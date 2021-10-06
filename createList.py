from flask import Flask, Blueprint, redirect, render_template, request, make_response, jsonify, json, session
from database import *
import re

createList = Blueprint("createList", __name__, static_folder="static",
                       template_folder="templates")


@createList.route("/", methods=["POST", "GET"])
def CreateList():
    return render_template("index.html", content="createList")


@app.route("/getEntryTypes", methods=["POST", "GET"])
def GetEntryTypes():
    found_entryType = EntryType.query.with_entities(EntryType.name).all()
    found_entryType = EntryTypeSchema(many=True).dump(found_entryType)

    return make_response(jsonify(found_entryType), 200)


@app.route("/createNewList", methods=["POST", "GET"])
def CreateNewList():
    found_user = User.query.filter_by(username=session["username"]).first()
    found_user = UserSchema(many=False).dump(found_user)
    userId = found_user["id"]

    found_entryType = EntryType.query.filter_by(
        name=request.form["entryType"]).first()
    found_entryType = EntryTypeSchema(many=False).dump(found_entryType)
    entryTypeId = found_entryType["id"]

    name = request.form["name"]

    image = request.form["image"]

    description = request.form["description"]

    newList = List(userId, entryTypeId, name, image, description)
    db.session.add(newList)
    db.session.commit()
    return render_template("index.html")
