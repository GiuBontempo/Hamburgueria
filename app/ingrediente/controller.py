from flask import request
from flask.views import MethodView
from app.ingrediente.models import Ingrediente

class IngredienteG(MethodView):
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


class IngredienteID(MethodView):
    def get(self, id):
        ingrediente = Ingrediente.query.get_or_404(id)
        return ingrediente.json()

    def patch(self, id):
        body = request.json
        ingrediente = Ingrediente.query.get_or_404(id)

        nome = body.get("nome", ingrediente.nome)
        quantidade = body.get("quantidade", ingrediente.quantidade)
        tipo = body.get("tipo", ingrediente.tipo)

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
