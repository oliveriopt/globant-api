from flask import Flask
from config import Config
from app.api import api
from app.db import init_db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    init_db(app)
    app.register_blueprint(api, url_prefix='/api')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
