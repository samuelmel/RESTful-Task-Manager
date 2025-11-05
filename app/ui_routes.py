from flask import Blueprint, render_template



bp_ui = Blueprint('ui', __name__, template_folder='templates', static_folder='static')

@bp_ui.route("/")
def index():
    return render_template("index.html")