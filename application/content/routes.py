import redis
from flask import Blueprint, render_template, request, make_response, session, jsonify, redirect, url_for
from flask_login import login_required
from application.landing_page.forms import Quiz

content_bp = Blueprint('content_bp', __name__)
conn = redis.Redis('localhost', 6379, charset='utf-8', decode_responses=True)
leader_board = 'leaderboard'


@content_bp.route('/points', methods=['POST'])
@login_required
def points():
    """Adds one point to user's cumulative points and returns a JSON response indicating success or failure"""
    if request.method == 'POST':
        r = request.get_json()
        mission_number = r.get('mission')  # Mission which was completed
        if mission_number in session['missions']:  # If mission is valid
            if not session['missions'][mission_number]:  # If mission has not been completed before
                session['points'] = session.get('points') + 1
                session['missions'][mission_number] = True
                conn.zadd(leader_board, {session['username']: 1}, incr=True)  # updating our leaderboard with new points
                return make_response(jsonify({'message': 'points received and updated'}), 200)
            return make_response(jsonify({'message': 'mission done'}), 200)
        return make_response(jsonify({'message': 'invalid mission'}), 200)
    return make_response(jsonify({'error': 'invalid request'}), 400)


@content_bp.route('/leaderboard', methods=['GET'])
@login_required
def leaderboard():
    """GET request returns sorted leaderboard"""
    top_10 = conn.zrevrangebyscore(leader_board, 15, 1, start=0, num=10, withscores=True)
    return jsonify(top_10)


@content_bp.route('/story', methods=['GET'])
@login_required
def story():
    """The story and avatar"""
    return render_template('story.html', username=session['username'][:12], xp=session.get('points'),
                           done=session['missions'].values())


@content_bp.route('/about', methods=['GET'])
@login_required
def about():
    return render_template('about.html')


@content_bp.route("/profile", methods=['GET'])
@login_required
def profile():
    completed = session['missions'].values()
    if False in completed:
        return render_template('profile.html', username=session['username'][:12], xp=session.get('points'),
                               done=completed)
    return render_template('profile.html', username=session['username'][:12], xp=session.get('points'),
                           done=completed, badge=True)


# Missions aka Content #
@content_bp.route('/mission_1', methods=['GET', 'POST'])
@login_required
def mission_1():
    """Mission 1 and its contents"""
    return render_template('mission_1.html', username=session['username'][:12], xp=session.get('points'),
                           done=session['missions'].values())


@content_bp.route('/mission_2', methods=['GET', 'POST'])
@login_required
def mission_2():
    """Mission 2 and its contents"""
    return render_template('mission_2.html', username=session['username'][:12], xp=session.get('points'),
                           done=session['missions'].values())


@content_bp.route('/mission_3', methods=['GET', 'POST'])
@login_required
def mission_3():
    """Mission 3 and its contents"""
    return render_template('mission_3.html', username=session['username'][:12], xp=session.get('points'),
                           done=session['missions'].values())


@content_bp.route('/mission_4', methods=['GET', 'POST'])
@login_required
def mission_4():
    """Mission 4 and its contents"""
    return render_template('mission_4.html', username=session['username'][:12], xp=session.get('points'),
                           done=session['missions'].values())


@content_bp.route('/mission_5', methods=['GET', 'POST'])
@login_required
def mission_5():
    """Mission 5 and its contents"""
    return render_template('mission_5.html', username=session['username'][:12], xp=session.get('points'),
                           done=session['missions'].values())


@content_bp.route('/mission_6', methods=['GET', 'POST'])
@login_required
def mission_6():
    """Mission 6 and its contents"""
    return render_template('mission_6.html', username=session['username'][:12], xp=session.get('points'),
                           done=session['missions'].values())


@content_bp.route('/mission_7', methods=['GET', 'POST'])
@login_required
def mission_7():
    """Mission 7 and its contents"""
    return render_template('mission_7.html', username=session['username'][:12], xp=session.get('points'),
                           done=session['missions'].values())


@content_bp.route('/sidemission', methods=['GET', 'POST'])
@login_required
def quiz():
    """Quiz route aka side mission"""
    form = Quiz()
    if request.method == 'POST':
        if form.validate_on_submit():
            if not session['missions']['special']:  # If mission has not been completed before
                session['points'] = session.get('points') + 6
                session['missions']['special'] = True
                conn.zadd(leader_board, {session['username']: 6}, incr=True)
            if session['points'] >= 10:
                return render_template('success.html', username=session['username'], xp=session.get('points'))
            return redirect(url_for('content_bp.profile'))

    return render_template('quiz.html', form=form, username=session['username'][:12], xp=session.get('points'),
                           done=session['missions'].values())


@content_bp.route('/links', methods=['GET'])
@login_required
def links():
    """Just some extra links for additional reading"""
    return render_template('extra_read_allaboutit.html')
