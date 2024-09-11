from flask import Blueprint
from controllers.employeeController import save, find_all, find_all_paginate, login

employee_blueprint = Blueprint('employee_bp', __name__)

employee_blueprint.route('/', methods=['POST'])(save)
employee_blueprint.route('/', methods=['GET'])(find_all)
employee_blueprint.route('/paginate', methods=['GET'])(find_all_paginate)
employee_blueprint.route('/login', methods=['POST'])(login)

