from flask import Blueprint
from app.funcionario.controller import FuncionarioG, FuncionarioID, IngredienteG_funcionario, IngredienteID_funcionario, ProdutoG_funcionario, ProdutoID_funcionario


funcionario_api = Blueprint("funcionario_api", __name__)

funcionario_api.add_url_rule('/cliente',view_func = FuncionarioG.as_view('funcionario_geral'), methods = ['GET', 'PATCH', 'DELETE'])
funcionario_api.add_url_rule('/cliente/<int:id>',view_func = FuncionarioID.as_view('funcionario_id'), methods = ['GET', 'PATCH', 'DELETE'])
funcionario_api.add_url_rule('/cliente',view_func = IngredienteG_funcionario.as_view('ingrediente_geral_funcionario'), methods = ['GET', 'PATCH', 'DELETE'])
funcionario_api.add_url_rule('/cliente/<int:id>',view_func = IngredienteID_funcionario.as_view('ingrediente_id_funcionario'), methods = ['GET', 'PATCH', 'DELETE'])
funcionario_api.add_url_rule('/cliente',view_func = ProdutoG_funcionario.as_view('produto_geral_funcionario'), methods = ['GET', 'PATCH', 'DELETE'])
funcionario_api.add_url_rule('/cliente/<int:id>',view_func = ProdutoID_funcionario.as_view('produto_id_funcionario'), methods = ['GET', 'PATCH', 'DELETE'])