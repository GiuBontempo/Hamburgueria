from app.models import BaseModel, db


class Funcionario(BaseModel):

    __tablename__ = "funcionario"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    nome = db.Column(db.String(70))
    email = db.Column(db.String(70), nullable = False, unique = True)
    senha = db.Column(db.String(70), nullable = False)


    def json(self):
        return{
            "nome":self.nome,
            "email":self.email,
            "senha":self.senha,
        }