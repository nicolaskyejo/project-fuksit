import redis
from flask import Blueprint, render_template, flash, url_for, redirect, request, session
from flask_login import login_required, current_user, logout_user, login_user
from application import login_manager
from .forms import LoginForm, SignupForm
from .models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import escape


auth_bp = Blueprint('auth_bp', __name__)
conn = redis.Redis('localhost')
leader_board = 'leaderboard'


@auth_bp.route('/signup', methods=['GET', 'POST'])
def register():
    signup_form = SignupForm(request.form)
    if request.method == 'POST':
        if signup_form.validate():
            username = request.form.get('username')
            escaped_username = escape(username)
            if username != escaped_username:
                flash('Invalid characters detected')
                return redirect(url_for('auth_bp.register'))
            password = request.form.get('password')
            existing_user = User.query.filter_by(username=username).first()
            if existing_user is None:  # if no users are found, this is a new user
                user = User(username=username, password=generate_password_hash(password, method='sha256'), admin=False)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                session['points'] = 0
                session['missions'] = {0: False, 1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False,
                                       'special': False}
                session['username'] = username
                return redirect(url_for('content_bp.story'))
            flash('Username taken')
            return redirect(url_for('auth_bp.register'))
    return render_template('signup.html', form=signup_form)


@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('content_bp.story'))  # If user is logged in, send them to the story page
    login_form = LoginForm(request.form)
    if request.method == 'POST':
        if login_form.validate():
            username = request.form.get('username')
            password = request.form.get('password')
            user = User.query.filter_by(username=username).first()
            if user:
                if check_password_hash(user.password, password):
                    login_user(user)
                    session['points'] = 0
                    session['missions'] = {0: False, 1: False, 2: False, 3: False, 4: False, 5: False, 6: False,
                                           7: False, 'special': False}
                    session['username'] = username
                    next = request.args.get('next')
                    return redirect(next or url_for('content_bp.story'))
            flash('Invalid Username/Password combination')
            return redirect(url_for('auth_bp.login'))
    return render_template('login_new.html', form=login_form)


@auth_bp.route('/cookie-policy', methods=['GET'])
def cookie():
    return render_template('cookie_policy.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    conn.zrem(leader_board, session['username'])  # remove username from leaderboard
    session.pop('username', None)
    return redirect(url_for('auth_bp.login'))


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('auth_bp.login'))
