from flask import Blueprint, render_template, flash, url_for, redirect, request, make_response, session
from flask_login import login_required, current_user


content_bp = Blueprint('content_bp', __name__)


# @app.route('/', methods=['GET', 'POST'])
# def login():
#     """The first page of the app"""
#     # Think about SSO login in case with get permission from Metropolia
#     if 'username' in session:  # if user is logged in
#         app.logger.info('User found in session')
#         return redirect(url_for('story'))
#     if request.method == 'POST':
#         username = request.form.get('username')
#         session['username'] = username  # user = request.form['username']
#         return redirect(url_for('story'))
#     return render_template('login.html')
#
#
# @app.route('/logout', methods=['POST'])
# def logout():
#     """Logs out the user by removing session"""
#     if 'logout' in request.form:
#         username = session['username']
#         session.pop('username', None)
#         app.logger.info(f'User {username} logged out')
#     return redirect(url_for('login'))


@content_bp.route('/story', methods=['GET'])
@login_required
def story():
    """The story and avatar"""
    return render_template('story.html', username=session['username'])


@content_bp.route('/about', methods=['GET'])
@login_required
def about():
    return render_template('about.html')


@content_bp.route("/profile")  # Edit later to make route correspond to the username
@login_required
def profile():
    return render_template('profile.html', username=session['username'])


# Missions aka Content #
@content_bp.route('/mission_1', methods=['GET', 'POST'])
@login_required
def mission_1():
    """Mission 1 and its contents"""
    return render_template('mission_1.html', username=session['username'])


@content_bp.route('/mission_2', methods=['GET', 'POST'])
@login_required
def mission_2():
    """Mission 2 and its contents"""
    return render_template('mission_2.html', username=session['username'])

# Error routes #
@content_bp.errorhandler(404)
def notfound():
    """404 template"""
    return make_response(render_template('404.html'), 404)

