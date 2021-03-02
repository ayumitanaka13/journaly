from datetime import datetime

from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_required, current_user
from flaskr.forms import JournalForm
from flaskr.models import User, Journal
from flaskr import db

add_journal_bp = Blueprint('add_journal', __name__, url_prefix='/add_journal') 

@add_journal_bp.route('', methods=['GET', 'POST'])
def add_journal():
    users = User.query.all()

    user_id = current_user.get_id()
    user = User.select_user_by_id(user_id)

    form = JournalForm(request.form)
    if request.method == 'POST' and form.validate():
        journal = Journal(
            start_date = form.start_date.data,
            end_date = form.end_date.data,
            country = form.counrty.data,
            city = form.city.data,
            title = form.title.data,
            comment = form.comment.data,
            picture_path_1 = form.picture_path_1.data,
            picture_path_2 = form.picture_path_2.data,
            picture_path_3 = form.picture_path_3.data
        )
        with db.session.begin(subtransactions=True):
            file = request.files[form.picture_path_1.name].read()
            if file:
                file_name = user_id + '_' + \
                    str(int(datetime.now().timestamp())) + '.jpg'
                picture_path_1 = 'flaskr/static/image_user/' + file_name
                open(picture_path_1, 'wb').write(file)
                journal.picture_path_1 = 'image_journal/' + file_name
            db.session.commit()
        with db.session.begin(subtransactions=True):
            journal.create_new_journal()
        db.session.commit()
        return redirect(url_for('journal.journal'))
    return render_template('add_journal/add_journal.html',  user=user, form=form)