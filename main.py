from create_player import create_player
from average import calc_average
from make_team import team_select
from random_select import rand_select
from count import pos_count
from sort_apt import APT_sort
from highest_apt import highest_APT
from lowest_avg import lowest_AVG
from flask import Flask,render_template,jsonify, request

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route("/create_player", methods=["POST"])
def handle_create_player():
    return create_player()


@app.route('/Average',methods=['POST'])
def handle_average():
    return calc_average()


@app.route('/make_team', methods=['POST'])
def handle_team_select():
    return team_select()


@app.route('/random_select', methods=['POST'])
def handle_rand_select():
    return rand_select()


@app.route('/count',methods=['GET'])
def handle_pos_count():
    return pos_count()


@app.route('/sort_apt', methods=['GET'])
def handle_APT_sort():
    return APT_sort()


@app.route('/highest_APT', methods=['GET'])
def handle_highest_APT():
    return highest_APT()


@app.route('/lowest_avg',methods=['GET'])
def handle_lowest_AVG():
    return lowest_AVG()