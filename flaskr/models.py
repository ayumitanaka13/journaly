from flaskr import db, login_manager
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
from sqlalchemy import and_, or_, desc
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from uuid import uuid4


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), index=True)
    password = db.Column(db.String(128))
    picture_path = db.Column(db.Text)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)

    @classmethod
    def select_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def validate_password(self, password):
        return check_password_hash(self.password, password)

    def create_new_user(self):
        db.session.add(self)

    @classmethod
    def select_user_by_id(cls, id):
        return cls.query.get(id)


class Journal(db.Model):

    __tablename__ = 'journals'

    id = db.Column(db.Integer, primary_key=True)
    from_user_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), index=True
    )
    start_date = db.Column(db.DateTime, nullable = False, default=datetime.strftime(datetime.today(), '%Y %b %d'))
    end_date = db.Column(db.DateTime, nullable = False, default=datetime.strftime(datetime.today(), '%Y %b %d'))
    country = db.Column(db.String(128))
    city = db.Column(db.String(128))
    title = db.Column(db.String(128))
    comment = db.Column(db.Text)
    picture_path_1 = db.Column(db.Text)
    picture_path_2 = db.Column(db.Text)
    picture_path_3 = db.Column(db.Text)

    def __init__(self, from_user_id, start_date, end_date, country, city, title, comment, picture_path_1, picture_path_2, picture_path_3):
        self.from_user_id = from_user_id
        self.start_date = start_date
        self.end_date = end_date
        self.country = country
        self.city = city
        self.title = title
        self.comment = comment
        self.picture_path_1 = picture_path_1
        self.picture_path_2 = picture_path_2
        self.picture_path_3 = picture_path_3

    def create_new_journal(self):
        db.session.add(self)


class LikeJournal(db.Model):

    __tablename__ = 'like_journals'

    id = db.Column(db.Integer, primary_key=True)
    from_user_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), index=True
    )
    to_journal_id = db.Column(
        db.Integer, db.ForeignKey('journals.id'), index=True
    )

    def __init__(self, from_user_id, to_journal_id):
        self.from_user_id = from_user_id
        self.to_journal_id = to_journal_id

    def add_like(self):
        db.session.add(self)

    def delete_like(self):
        db.session.delete(self)
    
    def is_liked(cls, journal_id):
        return cls.query.filter_by(
            from_user_id = current_user.get_id(),
            to_journal_id = journal_id
        ).count() > 0



class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    from_user_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), index=True
    )
    to_journal_id = db.Column(
        db.Integer, db.ForeignKey('journals.id'), index=True
    )
    comment = db.Column(db.Text)
    create_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, from_user_id, to_journal_id, comment):
        self.from_user_id = from_user_id
        self.to_journal_id = to_journal_id
        self.comment = comment

    def create_comment(self):
        db.session.add(self)