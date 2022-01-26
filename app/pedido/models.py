from app.models import BaseModel, db
from flask import Blueprint


pedido_api = Blueprint("pedido_api", __name__)


pedido_produto = db.Table("pedido_produto",
    db.Column("pedido_id", db.Integer, db.ForeignKey("pedido.id")),
    db.Column("produto_id", db.Integer, db.ForeignKey("produto.id"))
)


class Pedido(BaseModel):

    __tablename__ = "pedido"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    valor = db.Column(db.Float(15), nullable=False)
    valor_pos_desconto = db.Column(db.Float(15))

    cliente_id = db.Column(db.Integer, db.ForeignKey("cliente.id", unique = True))
    cupom_id = db.Column(db.Integer, db.ForeignKey('cupom.id'))
    cupom = db.relationship("Cupom", back_populates = "carrinhos")
    produtos = db.Relationship("Produto", secondary = pedido_produto, backref = "pedidos")

    def json(self):
        return{
            "valor":self.valor,
            "valor_pos_desconto":self.valor_pos_desconto
        }