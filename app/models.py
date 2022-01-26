from .extensions import db

class BaseModel(db.Model):

    __abstract__ = True


    def delete(obj):
        db.session.delete()
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()