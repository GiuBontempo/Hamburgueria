from app.models import BaseModel, db


class Ingrediente(BaseModel):

    __tablename__ = "ingrediente"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    nome = db.Column(db.String(70), nullable=False, unique=True)
    quantidade = db.Column(db.Integer(15), nullable=False)
    tipo = db.Column(db.string(30), nullable=False)


    def json(self):
        return{
            "nome":self.nome,
            "quantidade":self.quantidade,
            "tipo":self.tipo
        }