from app.funcionario.models import Funcionario
from flask import request, jsonify
from flask.views import MethodView

class FuncionarioG(MethodView):
    def post(self):
        body = request.json

        nome = body.get("nome")
        email = body.get("email")
        senha = body.get("senha")

        if isinstance(nome, str) and isinstance(email, str) and isinstance(senha, str):
            funcionario = Funcionario.query.filter_by(email=email) and Cliente.query.filter_by(cpf=cpf)
            if funcionario:
                return {"code_status":"esse funcionário já existe"},400
            funcionario = Cliente(nome=nome,email=email,senha=senha)
            funcionario.save()
            return funcionario.json(),200
        return {"code_status":"dados inválidos"},400
