from app.produto.models import Produto
from flask import request
from flask.views import MethodView

class ProdutoG(MethodView):
    def get(self):
        produtos = Produto.query.all()
        body = {}
        for produto in produtos:
            body[f"{produto.id}"] = produto.json()
        return body

    def post(self):
        body = request.json

        nome = body.get("nome")
        descricao = body.get("descricao")
        preco = body.get("preco")
        tipo = body.get("tipo")

        if isinstance(nome, str) and isinstance(descricao, str) and isinstance(tipo, str) and isinstance(preco, int):
            produto = Produto.query.filter_by(nome=nome).first()
            if produto:
                return {"code_status":"esse produto já existe"},400
            produto = Produto(nome=nome,descricao=descricao,preco=preco,tipo=tipo)
            produto.save()
            return produto.json(),200
        return {"code_status":"dados inválidos"},400


class ProdutoID(MethodView):
    def get(self, id):
        produto = Produto.query.get_or_404(id)
        return produto.json()

    def patch(self, id):
        body = request.json
        produto = Produto.query.get_or_404(id)

        nome = body.get("nome", produto.nome)
        descricao = body.get("descricao", produto.descricao)
        preco = body.get("preco", produto.preco)
        tipo = body.get("tipo", produto.tipo)

        if isinstance(nome, str) and isinstance(descricao, str) and isinstance(tipo, str) and isinstance(preco, int):
            produto.nome = nome
            produto.descricao = descricao
            produto.preco = preco
            produto.tipo = tipo
            produto.update()
            return produto.json(),200
        return {"code_status":"dados inválidos"},400

    def delete(self, id):
        produto = Produto.query.get_or_404(id)
        produto.delete(produto)
        return {"code_status":"deletado"},200
