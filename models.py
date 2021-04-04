"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

default_image = "http://tinyurl.com/demo-cupcake"


class Cupcake (db.Model):
    """ Model for Cupcakes """

    __tablename__ = 'cupcakes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default=default_image)

    def serialize(self):
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size' : self.size,
            'rating': self.rating,
            'image' : self.image
        }

    def __repr__(self):
        return f"<Cupcake {self.id} {self.flavor} {self.size} {self.rating} {self.image}>"