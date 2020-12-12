
from flask import Blueprint, request

from UtilitiesProvider import UtilitiesProvider


from repository.Repo import *
from flask_socketio import send

api = Blueprint('api_v1', __name__)



@api.route('/products')
def products():
    repo = UtilitiesProvider.repo
    list = repo.returnAllElems()
    result = []
    for i in list:
        result.append(i.toDict())

    return jsonify(result)

@api.route('/products/<id>')
def findOne(id):
    repo = UtilitiesProvider.repo
    elem :Product = repo.returnOne(id)

    return jsonify(elem.toDict())

@api.route('/products', methods=['POST'])
def addProduct():
    content = request.get_json()
    product = Product(**content)

    repo = UtilitiesProvider.repo
    repo.addProduct(product)

    return content

@api.route('/products', methods=['PUT'])
def updateProduct():
    content = request.get_json()
    product = Product(**content)

    print(product.toDict())

    repo = UtilitiesProvider.repo
    repo.updateProduct(product)

    return content



