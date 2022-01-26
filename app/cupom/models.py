from app.models import BaseModel, db


class Cupom(BaseModel):

    __tablename__ = "cupom"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    valor = db.Column(db.Integer, nullable = False)
    valor_minimo_do_pedido = db.Column(db.Integer)
    valor_maximo = db.Column(db.Integer)
    codigo = db.Column(db.String(70), nullable = False, unique = True)


    def json(self):
        return{
            "valor":self.valor,
            "valor_minimo_do_pedido":self.valor_minimo_do_pedido,
            "valor_maximo":self.valor_maximo,
            "codigo":self.codigo
        }