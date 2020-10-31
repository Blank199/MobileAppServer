from flask import Flask

from UtilitiesProvider import UtilitiesPtovide
from api.v1.api_v1 import api as api_v1
app = Flask(__name__)

UtilitiesPtovide.create()

app.register_blueprint(api_v1, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run()
