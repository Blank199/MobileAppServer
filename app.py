from flask import Flask, Blueprint
from flask_cors import CORS
from UtilitiesProvider import UtilitiesProvider
from api.v1.api_v1 import api as api_v1
from api.v1.sockets import mySocket

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)
mySocket.init_app(app)
UtilitiesProvider.create()
app.register_blueprint(api_v1, url_prefix='/api/v1')

api = Blueprint('api_v1', __name__)

if __name__ == '__main__':
    mySocket.run(app)
