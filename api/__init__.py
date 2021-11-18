import logging
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../database/sqlite.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
logging.basicConfig(level=logging.DEBUG)
db = SQLAlchemy(app)


@app.route("/")
def hello():
    return "My First API !!"
