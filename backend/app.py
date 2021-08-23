from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemySchema
from flask_marshmallow import Marshmallow
import os

__version__ = '0.1.0'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.environ.get('POSTGRES_USER')}:{os.environ.get('POSTGRES_PASSWORD')}@db:5432/{os.environ.get('POSTGRES_DB')}"
db = SQLAlchemy(app)
ma = Marshmallow()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

db.create_all()

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

@app.route('/')
def home():
    return 'home'

@app.get('/users/')
def get_users():
    users = User.query.all()
    return jsonify(UserSchema(many=True).dump(users))

@app.post('/users/')
def post_users():
    username = request.json['username']
    user = User(username=username)
    db.session.add(user)
    db.session.commit()
    return jsonify({ 'success': True })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
