from cgitb import html
from app.cliente.models import Cliente
from flask import request, render_template
from flask.views import MethodView
from flask_mail import Message
from app.extensions import mail, jwt
import bcrypt
from flask_jwt_extended import create_access_token, jwt_required


class ClienteG(MethodView):
    def post(self):
        body = request.json

        nome = body.get("nome")
        cpf = body.get("cpf")
        email = body.get("email")
        senha = body.get("senha")

        if isinstance(nome, str) and isinstance(cpf, str) and isinstance(email, str) and isinstance(senha, str):
            cliente = Cliente.query.filter_by(email=email).first() and Cliente.query.filter_by(cpf=cpf).first()
            if cliente:
                return {"code_status":"esse cliente já existe"},400
                
            senha_hash= bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
            cliente = Cliente(nome=nome,cpf=cpf,email=email,senha_hash=senha_hash)
            cliente.save()

            msg = Message(
                sender= 'giuliano.domiciano@poli.ufrj.br',
                recipients= [email],
                subject= "Bem vindo(a)!",
                html= render_template('email.html', nome=nome)
            )

            mail.send(msg)

            return cliente.json(),200
        return {"code_status":"dados inválidos"},400

    def get(self):
        clientes = Cliente.query.all()
        body = {}
        for cliente in clientes:
            body[f"{cliente.id}"] = cliente.json()
        return body


class ClienteID(MethodView):
    decorators = [jwt_required()]
    def get(self,id):
        cliente = Cliente.query.get_or_404(id)
        return cliente.json()

    def patch(self,id):
        body = request.json
        cliente = Cliente.query.get_or_404(id)

        nome = body.get("nome", cliente.nome)
        cpf = body.get("cpf", cliente.cpf)
        email = body.get("email", cliente.email)
        senha = body.get("senha", cliente.senha)
        cupons = body.get("cupons", cliente.cupons)

        if isinstance(nome, str) and isinstance(cpf, str) and isinstance(email, str) and isinstance(senha, str):
            
            senha_hash= bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
            
            cliente.nome = nome
            cliente.cpf = cpf
            cliente.email = email
            cliente.senha_hash = senha_hash
            cliente.cupons = cupons
            cliente.update()
            return cliente.json(),200
        return {"code_status":"dados inválidos"},400

    def delete(self, id):
        cliente = Cliente.query.get_or_404(id)
        cliente.delete(cliente)
        return {"code_status":"deletado"},200


class ClienteLogin(MethodView):
    def post(self):
        body = request.json

        email = body.get('email')
        senha = body.get('senha')

        cliente=Cliente.query.filter_by(email=email).first()

        if not cliente or not bcrypt.hashpw(senha.encode(), bcrypt.gensalt()):
            return {'code_status':'usuario ou senha invalidos!'}, 400

        token = create_access_token(identity=cliente.id)

        return {"token":token}, 200