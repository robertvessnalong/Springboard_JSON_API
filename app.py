"""Flask app for Cupcakes"""

from flask import Flask, json, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from models import db, connect_db, Cupcake


app = Flask(__name__)
cors = CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "hello-world"
app.config['CORS_HEADERS'] = 'Content-Type'
connect_db(app)


@app.route('/')
def render_page():
  return render_template('home.j2')

@app.route('/api/cupcakes')
def get_cupcakes():
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)

@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes', methods=["POST"])
def add_cupcake():
    try:
       new_cupcake = Cupcake(flavor=request.json['flavor'], size=request.json['size'], rating=request.json['rating'], image=request.json['image'] or None)
       db.session.add(new_cupcake)
       db.session.commit()
       return (jsonify(cupcake=new_cupcake.serialize()), 201)
    except:
        return jsonify(message='Sorry, please make sure all values are filled in.')

@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcake(id):
    try:
      cupcake = Cupcake.query.get_or_404(id)
      cupcake.flavor = request.json.get('flavor', cupcake.flavor)
      cupcake.size = request.json.get('size', cupcake.size)
      cupcake.rating = request.json.get('rating', cupcake.rating)
      cupcake.image = request.json.get('image', cupcake.image)
      db.session.commit()
      return jsonify(cupcake=cupcake.serialize())
    except:
      return jsonify(message='Sorry, please make sure all values are filled in.')

@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message=f"This cupcake has been deleted {cupcake}")