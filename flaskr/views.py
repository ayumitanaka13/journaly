from flask import Blueprint, render_template, redirect, url_for,request
from flaskr.models import Journal

bp = Blueprint('app', __name__, url_prefix='')

@bp.route('/')
def home():
    journals = Journal.query.all()
    return render_template('home.html', journals=journals)

@bp.app_errorhandler(404)
def page_not_found(e):
    return redirect(url_for('app.home'))

@bp.app_errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500