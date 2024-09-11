from flask import Blueprint
from controllers.userController import save, find_all, find_all_paginate, login

user_blueprint = Blueprint('user_bp', __name__)

user_blueprint.route('/', methods=['POST'])(save)
user_blueprint.route('/', methods=['GET'])(find_all)
user_blueprint.route('/paginate', methods=['GET'])(find_all_paginate)
user_blueprint.route('/login', methods=['POST'])(login)

