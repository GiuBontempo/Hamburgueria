from flask import Blueprint
from app.pedido.controller import PedidoID, PedidoG


pedido_api = Blueprint("pedido_api", __name__)


pedido_api.add_url_rule('/pedido',view_func = PedidoG.as_view('pedido_geral'), methods = ['POST', 'GET'])
pedido_api.add_url_rule('/pedido/<int:id>',view_func = PedidoID.as_view('pedido_id'), methods = ['GET', 'PATCH', 'DELETE'])