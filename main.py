from flask import Flask, render_template, url_for
from src.controllers import controllers

app = Flask(__name__)

@app.route("/")
def home():
    """
    Renders the home page with a form to input data and sections for fetching data.
    """
    return render_template("home.html")

# Register the blueprint
app.register_blueprint(controllers.bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
