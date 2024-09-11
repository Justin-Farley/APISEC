from flask import request, jsonify
from models.schemas.employeeSchema import employee_schema, employees_schema
from services import employeeService #dont import the individual function, import the module as a whole
from marshmallow import ValidationError
from caching import cache
from utils.util import token_required, admin_required

def login():
    try:
        credentials = request.json
        token = employeeService.login(credentials['username'], credentials['password'])
    except KeyError:
        return jsonify({'messages':'Invalid payload, expecting username and password'}), 401
    
    if token:
        return jsonify(token), 200
    else:
        return jsonify({'messages':'Invalid username or password'}), 401
    
    
@cache.cached(timeout=60)
@role_required
def save(): #name the controller will always be the same as the service function

    try:
        #try to validate the incoming data, and deserialize
        employee_data = employee_schema.load(request.json)

    except ValidationError as e:
        return jsonify(e.messages), 400
    
    employee_saved = employeeService.save(employee_data)
    return employee_schema.jsonify(employee_data), 201

# @token_required
@cache.cached(timeout=60)
@admin_required
def find_all():
    all_employees = employeeService.find_all()
    return employees_schema.jsonify(all_employees),200

def find_all_paginate():
    page = int(request.args.get('page'))
    per_page = int(request.args.get('per_page'))
    employees = employeeService.find_all_paginate(page, per_page)
    return employees_schema.jsonify(employees), 200