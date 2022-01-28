from app.cupom.models import Cupom
from flask import request
from flask.views import MethodView

class CupomG(MethodView):
    def get(self):
        cupons = Cupom.query.all()
        body = {}
        for cupom in cupons:
            body[f"{cupom.id}"] = cupom.json()
        return body

    def post(self):
        body = request.json

        valor = body.get("valor")
        valor_minimo_do_pedido = body.get("valor_minimo_do_pedido")
        valor_maximo = body.get("valor_maximo")
        codigo = body.get("codigo")

        if isinstance(valor, int) and isinstance(valor_minimo_do_pedido, int) and isinstance(valor_maximo, int) and isinstance(codigo, str):
            cupom = Cupom.query.filter_by(codigo=codigo).first()
            if cupom:
                return {"code_status":"esse cupom já existe"},400
            cupom = Cupom(valor=valor,valor_minimo_do_pedido=valor_minimo_do_pedido,valor_maximo=valor_maximo,codigo=codigo)
            cupom.save()
            return cupom.json(),200
        return {"code_status":"dados inválidos"},400


class CupomID(MethodView):
    def get(self, id):
        cupom = Cupom.query.get_or_404(id)
        return cupom.json()

    def patch(self, id):
        body = request.json
        cupom = Cupom.query.get_or_404(id)

        valor = body.get("valor", cupom.valor)
        valor_minimo_do_pedido = body.get("valor_minimo_do_pedido", cupom.valor_minimo_do_pedido)
        valor_maximo = body.get("valor_maximo", cupom.valor_maximo)
        codigo = body.get("codigo", cupom.codigo)

        if isinstance(valor, int) and isinstance(valor_minimo_do_pedido, int) and isinstance(valor_maximo, int) and isinstance(codigo, str):
            cupom.valor = valor
            cupom.valor_minimo_do_pedido = valor_minimo_do_pedido
            cupom.valor_maximo = valor_maximo
            cupom.codigo = codigo
            cupom.update()
            return cupom.json(),200
        return {"code_status":"dados inválidos"},400

    def delete(self, id):
        cupom = Cupom.query.get_or_404(id)
        cupom.delete(cupom)
        return {"code_status":"deletado"},200