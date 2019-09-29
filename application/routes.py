from flask import render_template, flash, url_for, redirect, request, make_response, session
from flask import current_app as app


@app.route('/', methods=['GET', 'POST'])
def login():
    """The first page of the app"""
    # Think about SSO login in case with get permission from Metropolia
    if 'username' in session:  # if user is logged in
        app.logger.info('User found in session')
        return redirect(url_for('story'))
    if request.method == 'POST':
        username = request.form.get('username')
        # user = request.form['username']
        session['username'] = username
        return redirect(url_for('story'))
    return render_template('login.html')


@app.route('/logout', methods=['POST'])
def logout():
    """Logs out the user by removing session"""
    if 'logout' in request.form:
        session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/story', methods=['GET'])
def story():
    """The story and avatar"""
    username = session['username']
    return render_template('story.html', username=username)


@app.errorhandler(404)
def notfound():
    """404 template"""
    return make_response(render_template('404.html'), 404)

# @app.route('/user/<username>')
# def profile(username):
