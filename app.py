from flask import Flask
from flask_cors import CORS

from UtilitiesProvider import UtilitiesProvider
from api.v1.api_v1 import api as api_v1


app = Flask(__name__)
CORS(app)

UtilitiesProvider.create()

app.register_blueprint(api_v1, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run()
