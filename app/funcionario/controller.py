from app.funcionario.models import Funcionario
from app.ingrediente.models import Ingrediente
from app.produto.models import Produto
from flask import request, jsonify
from flask.views import MethodView

class FuncionarioG(MethodView):
    def post(self):
        body = request.json

        nome = body.get("nome")
        email = body.get("email")
        senha = body.get("senha")

        if isinstance(nome, str) and isinstance(email, str) and isinstance(senha, str):
            funcionario = Funcionario.query.filter_by(email=email).first()
            if funcionario:
                return {"code_status":"esse funcionário já existe"},400
            funcionario = Funcionario(nome=nome,email=email,senha=senha)
            funcionario.save()
            return funcionario.json(),200
        return {"code_status":"dados inválidos"},400


class FuncionarioID(MethodView):
    def get(self,id):
        funcionario = Funcionario.query.get_or_404(id)
        return funcionario.json()

    def patch(self,id):
        body = request.json
        funcionario = Funcionario.query.get_or_404(id)

        nome = body.get("nome", funcionario.nome)
        email = body.get("email", funcionario.email)
        senha = body.get("senha", funcionario.senha)

        if isinstance(nome, str) and isinstance(email, str) and isinstance(senha, str):
            funcionario.nome = nome
            funcionario.email = email
            funcionario.senha = senha
            return funcionario.json(),200
        return {"code_status":"dados inválidos"},400

    def delete(self, id):
        funcionario = Funcionario.query.get_or_404(id)
        funcionario.delete(funcionario)
        return {"code_status":"deletado"},200

class IngredienteG_funcionario(MethodView):
    def get(self):
        ingredientes = Ingrediente.query.all()
        body = {}
        for ingrediente in ingredientes:
            body[f"{ingrediente.id}"] = ingrediente.json()
        return body

    def post(self):
        body = request.json

        nome = body.get("nome")
        quantidade = body.get("quantidade")
        tipo = body.get("tipo")

        if isinstance(nome, str) and isinstance(quantidade, int) and isinstance(tipo, str):
            ingrediente = Ingrediente.query.filter_by(nome=nome).first()
            if ingrediente:
                return {"code_status":"esse ingrediente já existe"},400
            ingrediente = Ingrediente(nome=nome,quantidade=quantidade,tipo=tipo)
            ingrediente.save()
            return ingrediente.json(),200
        return {"code_status":"dados inválidos"},400

class IngredienteID_funcionario(MethodView):
    def get(self, id):
        ingrediente = Ingrediente.query.get_or_404(id)
        return ingrediente.json()

    def patch(self, id):
        body = request.json
        ingrediente = Ingrediente.query.get_or_404(id)

        nome = body.get("nome", ingrediente.nome)
        quantidade = body.get("quantidade", ingrediente.quantidade)
        tipo = body.get("tipo", ingrediente.produtos)

        if isinstance(nome, str) and isinstance(quantidade, int) and isinstance(tipo, str):
            ingrediente.nome = nome
            ingrediente.quantidade = quantidade
            ingrediente.tipo = tipo
            ingrediente.update()
            return ingrediente.json(),200
        return {"code_status":"dados inválidos"},400

    def delete(self, id):
        ingrediente = Ingrediente.query.get_or_404(id)
        ingrediente.delete(ingrediente)
        return {"code_status":"deletado"},200

class ProdutoG_funcionario(MethodView):
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

class ProdutoID_funcionario(MethodView):
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