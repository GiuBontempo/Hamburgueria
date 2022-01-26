from app.cliente.models import Cliente
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
