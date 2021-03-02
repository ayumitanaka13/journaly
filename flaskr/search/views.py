from flask import Blueprint, render_template, request, redirect, url_for, session
from flaskr.models import Journal
from flaskr.forms import SearchForm

search_bp = Blueprint('search', __name__, url_prefix='/search')

@search_bp.route('', methods=['GET', 'POST'])
def search():
    journals = Journal.query.all()
    form = SearchForm(request.form)

    if request.method == 'POST' and form.validate():
        keyword = form.keyword.data
    return render_template('search/search.html', journals=journals, form=form)