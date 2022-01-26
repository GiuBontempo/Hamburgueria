from app.cliente.models import Cliente
from app.pedido.models import Pedido
from app.produto.models import Produto
from flask import request, jsonify
from flask.views import MethodView

class ClienteG(MethodView):
    def post(self):
        body = request.json

        nome = body.get("nome")
        cpf = body.get("cpf")
        email = body.get("email")
        senha = body.get("senha")

        if isinstance(nome, str) and isinstance(cpf, str) and isinstance(email, str) and isinstance(senha, str):
            cliente = Cliente.query.filter_by(email=email) and Cliente.query.filter_by(cpf=cpf)
            if cliente:
                return {"code_status":"esse cliente já existe"},400
            cliente = Cliente(nome=nome,cpf=cpf,email=email,senha=senha)
            cliente.save()
            return cliente.json(),200
        return {"code_status":"dados inválidos"},400


class ClienteID(MethodView):
    def get(self,id):
        cliente = Cliente.query.get_or_404(id)
        return cliente.json()

    def patch(self,id):
        body = request.json
        cliente = Cliente.query.get_or_404

        nome = body.get("nome", cliente.nome)
        cpf = body.get("cpf", cliente.cpf)
        email = body.get("email", cliente.email)
        senha = body.get("senha", cliente.senha)
        cupons = body.get("cupons", cliente.cupons)

        if isinstance(nome, str) and isinstance(cpf, str) and isinstance(email, str) and isinstance(senha, str):
            cliente.nome = nome
            cliente.cpf = cpf
            cliente.email = email
            cliente.senha = senha
            cliente.cupons = cupons
            return cliente.json(),200
        return {"code_status":"dados inválidos"},400

    def delete(self, id):
        cliente = Cliente.query.get_or_404
        cliente.delete(cliente)
        return {"code_status":"deletado"},200


class PedidoID_user(MethodView):
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

class ProdutoG_user(MethodView):
    def get(self):
        produtos = Produto.query.all()
        body = {}
        for produto in produtos:
            body[f"{produto.id}"] = produto.json()
        return body