from flask_wtf import FlaskForm
from wtforms.form import Form
from wtforms.fields import (
    StringField, FileField, PasswordField, DateField, MultipleFileField,
    SelectField, SubmitField, HiddenField, TextAreaField
)
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flaskr.models import User, Journal


class LoginForm(FlaskForm):
    email = StringField(
        'Mail', validators=[DataRequired(), Email('Your email adress is not correct.')]
    )
    password = PasswordField(
        'Password', validators=[DataRequired()]
    )
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    email = StringField(
        'Mail', validators=[DataRequired(), Email()]
    )
    username = StringField(
        'Name', validators=[DataRequired()]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), EqualTo('password_confirm', message='Your password is not correct.')]
    )
    password_confirm = PasswordField(
        'Password again', validators=[DataRequired()]
    )
    submit = SubmitField('Sign up')

    def validate_email(self, field):
        if User.select_user_by_email(field.data):
            raise ValidationError('Your email adress is already registered.')


class UserForm(FlaskForm):
    picture_path = FileField('', validators=[DataRequired()])
    submit = SubmitField('Submit')


class JournalForm(FlaskForm):
    from_user_id = HiddenField()
    start_date = DateField('Start', format='%Y/%m/%d', validators=[DataRequired()])
    end_date = DateField('End', format='%Y/%m/%d', validators=[DataRequired()])
    country = SelectField(
        'Country',
        choices=[u'Country', ('Brazil'), ('Canada'), ('Japan'), ('Singapore'), ('Spain')],
        validators=[DataRequired()]
    )
    city = SelectField(
        'City',
        choices=[u'City', ('Barcelona'), ('Kyoto'), ('Rio de Janeiro'), ('Singapore'), ('Vancouver')],
        validators=[DataRequired()]
    )
    title = StringField(
        'Title', validators=[DataRequired()]
    )
    comment = TextAreaField(
        'Journal', validators=[DataRequired()]
    )
    picture_path = FileField('', validators=[DataRequired()])
    submit = SubmitField('Submit')


class LikeJournalForm(FlaskForm):
    from_user_id = HiddenField()
    to_journal_id = HiddenField()
    submit = SubmitField('♡ Like')


class CommentForm(FlaskForm):
    to_journal_id = HiddenField()
    comment = TextAreaField(
        '', validators=[DataRequired()]
    )
    submit = SubmitField('Add Comment')


class SearchForm(FlaskForm):
    keyword = StringField(
        '', validators=[DataRequired()]
    )
    submit = SubmitField('Search')