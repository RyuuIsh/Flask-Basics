from flask import Blueprint

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    return "<h1>Welcome to the Flask Blueprint App!</h1>"

@main_bp.route("/about")
def about():
    return "<h2>About Page</h2><p>This is a modular Flask app using Blueprints.</p>"
