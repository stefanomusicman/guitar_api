from flask import Blueprint, request, jsonify

guitar = Blueprint("guitar", __name__)


# ADD A NEW GUITAR
@guitar.route("/v0/guitars/", methods=["POST"])
def add():
    pass




# GET ALL GUITARS
@guitar.route("/v0/guitars/", methods=["GET"])
def fetchAll():
    pass