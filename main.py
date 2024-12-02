from flask import Flask
from src.controllers import controllers

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Hello, World!</p>"

# Register the blueprint
app.register_blueprint(controllers.bp, url_prefix="/api")
