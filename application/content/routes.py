import redis
from flask import Blueprint, render_template, flash, url_for, redirect, request, make_response, session, jsonify
from flask_login import login_required, current_user


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
    return render_template('story.html', username=session['username'], xp=session.get('points'))


@content_bp.route('/about', methods=['GET'])
@login_required
def about():
    return render_template('about.html')


@content_bp.route("/profile")
@login_required
def profile():
    return render_template('profile.html', username=session['username'])


# Missions aka Content #
@content_bp.route('/mission_1', methods=['GET', 'POST'])
@login_required
def mission_1():
    """Mission 1 and its contents"""
    return render_template('mission_1.html', username=session['username'], xp=session.get('points'))


@content_bp.route('/mission_2', methods=['GET', 'POST'])
@login_required
def mission_2():
    """Mission 2 and its contents"""
    return render_template('mission_2.html', username=session['username'], xp=session.get('points'))



