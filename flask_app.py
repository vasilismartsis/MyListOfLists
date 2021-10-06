from flask import Flask, redirect, url_for, render_template, request, jsonify, make_response, Blueprint
from flask_sqlalchemy import SQLAlchemy
import re

from account import account
from createList import createList
from database import *

app.register_blueprint(account, url_prefix="/account")
app.register_blueprint(createList, url_prefix="/createList")

app.secret_key = "mySecretKey"

# routes
@app.route("/")
def index():
    return render_template("index.html", sks=3)


if __name__ == "__main__":
    db.create_all()
    app.debug = True
    app.run(host='0.0.0.0', port=5005)
