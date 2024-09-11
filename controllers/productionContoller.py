from flask import jsonify, request
from models.schemas.productionSchema import production_schema, productions_schema
from marshmallow import ValidationError
from services import productionService


@cache.cached(timeout=60)
@role_required
def save():
    try:
        production_data = production_schema.load(request.json)
    except ValidationError as err:
            return jsonify(err.message), 400
    try:
         production_save = productionService.save(production_data)
         return production_schema.jsonify(production_save), 201
    except ValidationError as e:
         return jsonify({"error": str(e)}), 400

def find_all():
     all_productions = productionService.find_all()
     return productions_schema.jsonify(all_productions), 200

def search_production():
     search_term = request.args.get("search")
     searched_items = productionService.search_production(search_term)
     return productions_schema.jsonify(searched_items)