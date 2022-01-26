from app.models import BaseModel, db
from flask import Blueprint


produto_api = Blueprint("produto_api", __name__)


class Produto(BaseModel):

    __tablename__ = "produto"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    nome = db.Column(db.String(70), nullable=False)
    descricao = db.Column(db.String(1000))
    preco = db.Column(db.Float(15), nullable=False)
    tipo = db.Column(db.String(30), nullable=False)


    def json(self):
        return{
            "nome":self.nome,
            "descricao":self.descricao,
            "preco":self.preco,
            "tipo":self.tipo
        }