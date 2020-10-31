from flask import Blueprint, jsonify

from UtilitiesProvider import UtilitiesPtovide
from repository.Repo import *

api = Blueprint('api_v1', __name__)



@api.route('/products')
def products():
    repo = UtilitiesPtovide.repo
    list = repo.returnAllElems()
    result = []
    for i in list:
        result.append(i.toDict())

    return jsonify(result)
