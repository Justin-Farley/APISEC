from flask import Blueprint
from controllers.productionController import find_all, save, search_production

production_blueprint = Blueprint('production_bp', __name__)
production_blueprint.route('/', methods=['POST'])(save)
production_blueprint.route('/', methods=['GET'])(find_all)
production_blueprint.route('/search', methods=['GET'])(search_production)