from flask import Blueprint

user_bp = Blueprint("user", __name__)

@user_bp.route("/profile")
def profile():
    return "<h1>User Profile Page</h1>"

@user_bp.route("/settings")
def settings():
    return "<h1>User Settings Page</h1>"
