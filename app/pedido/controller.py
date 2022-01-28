from flask import request
from flask.views import MethodView
from app.pedido.models import Pedido


class PedidoG(MethodView):
    def get(self):
        pedidos = Pedido.query.all()
        body = {}
        for pedido in pedidos:
            body[f"{pedido.id}"] = pedido.json()
        return body

    def post(self):
        body = request.json

        valor = body.get("valor")
        valor_pos_desconto = body.get("valor_pos_desconto")

        if isinstance(valor, int) and isinstance(valor_pos_desconto, int):
            pedido = Pedido(valor=valor, valor_pos_desconto=valor_pos_desconto)
            pedido.save()
            return pedido.json(),200
        return {"code_status":"dados inválidos"},400


class PedidoID(MethodView):
    def get(self, id):
        pedido = Pedido.query.get_or_404(id)
        return pedido.json()

    def patch(self, id):
        body = request.json
        pedido = Pedido.query.get_or_404(id)

        cupom = body.get("cupom", pedido.cupom)
        produtos = body.get("produtos", pedido.produtos)

        pedido.cupom = cupom
        pedido.produtos = produtos
        pedido.update()
        return pedido.json(),200

    def delete(self, id):
        pedido = Pedido.query.get_or_404(id)
        pedido.delete(pedido)
        return {"code_status":"deletado"},200