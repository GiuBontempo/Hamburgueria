from app.models import BaseModel, db


cliente_cupom = db.Table("cliente_cupom",
    db.Column("cliente_id", db.Integer, db.ForeignKey("cliente.id")),
    db.Column("cupom_id", db.Integer, db.ForeignKey("cupom.id"))
)


class Cliente(BaseModel):

    __tablename__ = "cliente"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    nome = db.Column(db.String(70))
    cpf = db.Column(db.String(15), nullable = False, unique = True)
    email = db.Column(db.String(70), nullable = False, unique = True)
    senha = db.Column(db.String(70), nullable = False)

    pedido = db.relationship("Carrinho", backref="cliente", uselist = False)
    cupons = db.relationship("Cupom", secondary = cliente_cupom, backref = "clientes")

    def json(self):
        return{
            "nome":self.nome,
            "cpf":self.cpf,
            "email":self.email,
            "senha":self.senha,
        }