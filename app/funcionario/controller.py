from app.funcionario.models import Funcionario
from flask import request
from flask.views import MethodView
from app.extensions import jwt
import bcrypt
from flask_jwt_extended import create_access_token, jwt_required


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

            senha_hash= bcrypt.hashpw(senha.encode(), bcrypt.gensalt())

            funcionario = Funcionario(nome=nome,email=email,senha_hash=senha_hash)
            funcionario.save()
            return funcionario.json(),200
        return {"code_status":"dados inválidos"},400


class FuncionarioID(MethodView):
    decorators = [jwt_required()]
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

            senha_hash= bcrypt.hashpw(senha.encode(), bcrypt.gensalt())

            funcionario.nome = nome
            funcionario.email = email
            funcionario.senha_hash = senha_hash
            return funcionario.json(),200
        return {"code_status":"dados inválidos"},400

    def delete(self, id):
        funcionario = Funcionario.query.get_or_404(id)
        funcionario.delete(funcionario)
        return {"code_status":"deletado"},200


class FuncionarioLogin(MethodView):
    def post(self):
        body = request.json

        email = body.get('email')
        senha = body.get('senha')

        funcionario=Funcionario.query.filter_by(email=email).first()

        if not funcionario or not bcrypt.hashpw(senha.encode(), bcrypt.gensalt()):
            return {'code_status':'usuario ou senha invalidos!'}, 400

        token = create_access_token(identity=funcionario.id)

        return {"token":token}, 200