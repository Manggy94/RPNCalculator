from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint

from app.resources.calculator import Calculator

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Calculator, "/api/stack", '/api/stack/<string:operation>')

swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


if __name__ == "__main__":
    app.run(debug=True)