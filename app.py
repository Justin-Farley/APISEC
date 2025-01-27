from flask import Flask
from database import db
from models.schemas import ma
# from limiter import limiter
from caching import cache
from flask_swagger_ui import get_swaggerui_blueprint

from models.customer import Customer
from models.product import Product
from models.order import Order
from models.employee import Employee

from routes.customerBP import customer_blueprint
from routes.productBP import product_blueprint
from routes.orderBP import order_blueprint
from routes.employeeBP import employee_blueprint

#SWAGGER
SWAGGER_URL = '/api/docs' # URL endpoint for Swagger API documentation
API_URL = '/static/swagger.yaml'

swagger_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name':"E-commerce API"})

def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)
    # limiter.init_app(app)
    cache.init_app(app)

    print('Running')
    return app

def blueprint_config(app):
    app.register_blueprint(customer_blueprint, url_prefix='/customers')
    app.register_blueprint(product_blueprint, url_prefix='/products')
    app.register_blueprint(order_blueprint, url_prefix='/orders')
    app.register_blueprint(employee_blueprint, url_prefix='/employees')
    
    app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)



if __name__ == '__main__':
    app = create_app('DevelopmentConfig')

    blueprint_config(app)

    

    with app.app_context():
        
        db.create_all()

    app.run()