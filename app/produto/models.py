from app.models import BaseModel, db


class Produto(BaseModel):

    __tablename__ = "produto"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    nome = db.Column(db.String(70), nullable=False, unique=True)
    descricao = db.Column(db.String(1000))
    preco = db.Column(db.Float(15), nullable=False)
    tipo = db.Column(db.string(30), nullable=False)


    def json(self):
        return{
            "nome":self.nome,
            "descricao":self.descricao,
            "preco":self.preco,
            "tipo":self.tipo
        }