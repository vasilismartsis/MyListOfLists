from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# Sql
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MyRecipeList.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(200))
    password = db.Column(db.String(200))

    children = db.relationship("List")

    def __init__(self, username, password):
        self.username = username
        self.password = password


class EntryType(db.Model):
    __tablename__ = 'entryType'
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(200))
    image = db.Column(db.String(200))
    link = db.Column(db.String(200))
    description = db.Column(db.String(2000))

    children = db.relationship("List")
    children = db.relationship("Entry")

    def __init__(self, name, image, link, description):
        self.name = name
        self.image = image
        self.link = link
        self.description = description


class List(db.Model):
    __tablename__ = 'list'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    entryTypeId = db.Column(db.Integer, db.ForeignKey('entryType.id'))

    name = db.Column(db.String(200))
    image = db.Column(db.String(200))
    description = db.Column(db.String(2000))

    children = db.relationship("Entry")

    def __init__(self, userId, entryTypeId, name, image, description):
        self.userId = userId
        self.entryTypeId = entryTypeId
        self.name = name
        self.image = image
        self.description = description


class Entry(db.Model):
    __tablename__ = 'entry'
    id = db.Column(db.Integer, primary_key=True)
    listId = db.Column(db.Integer, db.ForeignKey('list.id'))
    entryTypeId = db.Column(db.Integer, db.ForeignKey('entryType.id'))

    entryValue = db.Column(db.String(200))
    image = db.Column(db.String(200))
    link = db.Column(db.String(200))
    description = db.Column(db.String(2000))

    def __init__(self, name, image, link, description):
        self.name = name
        self.image = image
        self.link = link
        self.description = description


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User


class EntryTypeSchema(ma.ModelSchema):
    class Meta:
        model = EntryType


class ListSchema(ma.ModelSchema):
    class Meta:
        model = List
