from flask import Flask
from .config import Config
from .extensions import db, migrate
from app.cliente.routes import cliente_api
from app.funcionario.routes import funcionario_api
from app.cupom.models import cupom_api
from app.ingrediente.models import ingrediente_api
from app.pedido.models import pedido_api
from app.produto.models import produto_api

def create_app():

    app=Flask(__name__)
    app.config.from_object(Config)
    app.debug=True

    db.init_app(app)
    migrate.init_app(app,db)

    app.register_blueprint(cliente_api)
    app.register_blueprint(funcionario_api)
    app.register_blueprint(cupom_api)
    app.register_blueprint(ingrediente_api)
    app.register_blueprint(pedido_api)
    app.register_blueprint(produto_api)

    return app