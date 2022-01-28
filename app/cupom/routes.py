from flask import Blueprint
from app.cupom.controller import CupomG, CupomID

cupom_api = Blueprint("cupom_api", __name__)

cupom_api.add_url_rule('/cupom',view_func = CupomG.as_view('cupom_geral'), methods = ['GET', 'POST'])
cupom_api.add_url_rule('/cupom/<int:id>',view_func = CupomID.as_view('cupom_id'), methods = ['GET', 'PATCH', 'DELETE'])