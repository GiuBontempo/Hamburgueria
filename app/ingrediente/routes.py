from flask import Blueprint
from app.ingrediente.controller import IngredienteG, IngredienteID

ingrediente_api = Blueprint("ingrediente_api", __name__)

ingrediente_api.add_url_rule('/ingrediente',view_func = IngredienteG.as_view('ingrediente_geral'), methods = ['GET', 'POST'])
ingrediente_api.add_url_rule('/ingrediente/<int:id>',view_func = IngredienteID.as_view('ingrediente_id'), methods = ['GET', 'PATCH', 'DELETE'])