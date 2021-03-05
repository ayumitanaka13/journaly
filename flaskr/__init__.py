import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'login.login'
login_manager.login_message = 'Please login'

basedir = os.path.abspath(os.path.dirname(__name__))
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = 'SECRET_KEY'
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    # app.config['SQLALCHEMY_DATABASE_URL'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    from flaskr.login.views import login_bp
    from flaskr.logout.views import logout_bp
    from flaskr.signup.views import signup_bp
    from flaskr.user.views import user_bp
    from flaskr.search.views import search_bp
    from flaskr.journal.views import journal_bp
    from flaskr.add_journal.views import add_journal_bp
    from flaskr.contact.views import contact_bp
    app.register_blueprint(login_bp)
    app.register_blueprint(logout_bp)
    app.register_blueprint(signup_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(journal_bp)
    app.register_blueprint(add_journal_bp)
    app.register_blueprint(contact_bp)

    from flaskr.views import bp
    app.register_blueprint(bp)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    return app