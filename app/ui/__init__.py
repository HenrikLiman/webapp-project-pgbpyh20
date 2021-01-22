from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)
    from app.ui.routes import index
    app.register_blueprint(index.bp)
    from app.ui.routes import place
    app.register_blueprint(place.bp)
    from app.ui.routes import map
    app.register_blueprint(map.bp)
    from app.ui.routes import api
    app.register_blueprint(api.bp)
    app.add_url_rule('/', endpoint='index')

    return app
