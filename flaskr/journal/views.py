from flask import Blueprint, request, render_template, flash
from flask_login import login_required, current_user
from flaskr.forms import CommentForm, LikeJournalForm
from flaskr.models import Journal, User, Comment, LikeJournal
from flaskr import db

journal_bp = Blueprint('journal', __name__, url_prefix='/journal') 

@journal_bp.route('', methods=['GET', 'POST'])
def journal():
    users = User.query.all()
    journals = Journal.query.all()
    comments = Comment.query.all()
    like_journals = LikeJournal.query.all()

    user_id = current_user.get_id()
    user = User.select_user_by_id(user_id)

    form = LikeJournalForm(request.form)
    form_c = CommentForm(request.form)

    if request.method == 'POST' and form.validate():
        new_like = LikeJournal(user_id, form.to_journal_id.data)
        with db.session.begin(subtransactions=True):
            if new_like.is_liked(form.to_journal_id.data) == False:
                new_like.add_like()
            else:
                liked_items = LikeJournal.query.filter_by(
                    from_user_id = user_id,
                    to_journal_id = form.to_journal_id.data
                ).all()
                for liked_item in liked_items:
                    liked_item.delete_like()
        db.session.commit()

    if request.method == 'POST' and form_c.validate():
        new_comment = Comment(user_id, form_c.to_journal_id.data, form_c.comment.data)
        with db.session.begin(subtransactions=True):
            new_comment.create_comment()
        db.session.commit()
        flash("Your comment has been added!", "success")
    return render_template('journal/journal.html',  users=users, journals=journals, comments=comments, like_journals=like_journals, form=form, form_c=form_c)