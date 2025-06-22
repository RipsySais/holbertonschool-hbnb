from app import create_app
from flask import Flask
from app.api import bp_api
app = create_app()
app = Flask(__name__)
app.register_blueprint(bp_api)


if __name__ == '__main__':
    app.run(debug=True)
