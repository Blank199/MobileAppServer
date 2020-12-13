# from flask import Flask
# from flask_cors import CORS
#
# from UtilitiesProvider import UtilitiesProvider
# from api.v1.api_v1 import api as api_v1
#
#
# app = Flask(__name__)
# CORS(app)
#
# UtilitiesProvider.create()
#
# app.register_blueprint(api_v1, url_prefix='/api/v1')
#
# if __name__ == '__main__':
#     app.run()

from flask import Flask, Blueprint
from flask_socketio import SocketIO
from flask_cors import CORS
from UtilitiesProvider import UtilitiesProvider
from api.v1.api_v1 import api as api_v1

app = Flask(__name__)
UtilitiesProvider.create()
app.register_blueprint(api_v1, url_prefix='/api/v1')
app.config['SECRET_KEY'] = 'secret!'
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)
mySocket = SocketIO(app, cors_allowed_origins="*")

api = Blueprint('api_v1', __name__)

if __name__ == '__main__':
    mySocket.run(app)
