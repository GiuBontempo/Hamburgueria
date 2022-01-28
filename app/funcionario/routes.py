from flask import Blueprint
from app.funcionario.controller import FuncionarioG, FuncionarioID


funcionario_api = Blueprint("funcionario_api", __name__)

funcionario_api.add_url_rule('/funcionario',view_func = FuncionarioG.as_view('funcionario_geral'), methods = ['POST'])
funcionario_api.add_url_rule('/funcionario/<int:id>',view_func = FuncionarioID.as_view('funcionario_id'), methods = ['GET', 'PATCH', 'DELETE'])