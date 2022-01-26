from flask import Blueprint
from app.cliente.controller import ClienteG, ClienteID, PedidoID_user, ProdutoG_user


cliente_api = Blueprint("cliente_api", __name__)

cliente_api.add_url_rule('/cliente',view_func = ClienteG.as_view('cliente_geral'), methods = ['POST', 'GET'])
cliente_api.add_url_rule('/cliente/<int:id>',view_func = ClienteID.as_view('cliente_id'), methods = ['GET', 'PATCH', 'DELETE'])
cliente_api.add_url_rule('/cliente/pedido/<int:id>',view_func = PedidoID_user.as_view('pedido_id_user'), methods = ['GET', 'PATCH'])
cliente_api.add_url_rule('/cliente/produto',view_func = ProdutoG_user.as_view('produto_geral_user'), methods = ['GET'])