from flask import Blueprint, render_template, flash, url_for, redirect, request, session
from flask_login import login_required, current_user, logout_user, login_user
from application import login_manager
from .forms import LoginForm, SignupForm
from .models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/signup', methods=['GET', 'POST'])
def register():
    signup_form = SignupForm(request.form)
    if request.method == 'POST':
        if signup_form.validate():
            username = request.form.get('username')
            password = request.form.get('password')
            existing_user = User.query.filter_by(username=username).all()
            if existing_user is None:  # if no users are found, this is a new user
                user = User(username=username, password=generate_password_hash(password, method='sha256'), admin=False)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                session['username'] = username
                return redirect(url_for('content_bp.story'))
            else:
                for user in existing_user:
                    if check_password_hash(user.password, password):
                        flash('Username/Password is incorrect')
                        return redirect(url_for('auth_bp.register'))
                # username is the same but password is different
                user = User(username=username, password=generate_password_hash(password, method='sha256'),
                            admin=False)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                session['username'] = username
                return redirect(url_for('content_bp.story'))

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
            user = User.query.filter_by(username=username).all()
            if user:
                for valid_user in user:
                    if check_password_hash(valid_user.password, password):
                        login_user(valid_user)
                        session['username'] = username
                        next = request.args.get('next')
                        return redirect(next or url_for('content_bp.story'))
                    else:
                        pass
        flash('Invalid Username/Password combination')
        return redirect(url_for('auth_bp.login'))
    return render_template('login_new.html', form=login_form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
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


# def login():
#     """The first page of the app"""
#     # Think about SSO login in case with get permission from Metropolia
#     if 'username' in session:  # if user is logged in
#         return redirect(url_for('content_bp.story'))
#     if request.method == 'POST':
#         username = request.form.get('username')
#         session['username'] = username  # user = request.form['username']
#         return redirect(url_for('content_bp.story'))
#     return render_template('login.html')
#
#
# @auth_bp.route('/logout', methods=['POST'])
# def logout():
#     """Logs out the user by removing session"""
#     if 'logout' in request.form:
#         session.pop('username', None)
#     return redirect(url_for('auth_bp.login'))

