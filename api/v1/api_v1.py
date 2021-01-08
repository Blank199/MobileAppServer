import json

from flask import Blueprint, request

from Utilities.Tocken import createToken, verify
from UtilitiesProvider import UtilitiesProvider
from domain.User import User

from repository.Repo import *

api = Blueprint('api_v1', __name__)

def getUsername():
    token = request.headers['Authorization'].split(" ")[1]
    credentials = json.loads(verify(token))
    return credentials['username']

@api.route('/products/<limit>/<page>')
def products(limit, page):
    username = getUsername()
    repo = UtilitiesProvider.repo
    list = repo.returnAllElems(username, int(limit), int(page))
    result = []
    for i in list:
        result.append(i.toDict())

    return jsonify(result)


@api.route('/products/<id>')
def findOne(id):
    repo = UtilitiesProvider.repo
    elem: Product = repo.returnOne(id)

    return jsonify(elem.toDict())


@api.route('/products', methods=['POST'])
def addProduct():
    repo = UtilitiesProvider.repo
    content = request.get_json()
    print('POST - ')
    print(content)
    product = Product(**content)
    product.username = getUsername()
    product.id = repo.noProducts().__str__()
    repo.addProduct(product)

    return content


@api.route('/products', methods=['PUT'])
def updateProduct():
    content = request.get_json()
    product = Product(**content)
    product.username = getUsername()
    print('PUT - ')
    print(product.toDict())

    repo = UtilitiesProvider.repo
    repo.updateProduct(product)

    return content


@api.route('/login', methods=['POST'])
def login():
    content = request.get_json()
    user = User(**content)

    userRepo = UtilitiesProvider.userRepo
    result = userRepo.verifyLogin(user)

    if result != None:
        return {'token': createToken(content)}

    return "Username or password are wrong"
