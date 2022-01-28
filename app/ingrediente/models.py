from app.models import BaseModel, db
from flask import Blueprint


class Ingrediente(BaseModel):

    __tablename__ = "ingrediente"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    nome = db.Column(db.String(70), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(30), nullable=False)


    def json(self):
        return{
            "nome":self.nome,
            "quantidade":self.quantidade,
            "tipo":self.tipo
        }