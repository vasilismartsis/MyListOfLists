from flask import Blueprint, render_template, request, session
from database import *

logout = Blueprint("logout", __name__, static_folder="static",
                   template_folder="templates")


@logout.route("/")
def logoutAction():
    session.clear()
    return render_template("index.html")
