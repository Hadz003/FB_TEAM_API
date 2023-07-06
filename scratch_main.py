from create_player import create_player
from average import calc_average
from make_team import team_select
from random_select import rand_select
from count import pos_count
from sort_apt import APT_sort
from highest_apt import highest_APT
from lowest_avg import lowest_AVG
from flask import Flask, jsonify, request

print("Welcome to the Football Team Program!!\n")

app = Flask(__name__)

num=1
while num !=0:

    print("\nChoose one of the options below:\n\n1. Create a new player\n2. Get a player's average\n3. Make a team of 10 players\n4. Randomly select players\n5. Count players based on position\n6. Sort all players by APT from high to low\n7. Find the player with the highest APT score\n8. Find the player with lowest AVG score\n\nPress 0 to exit the program ")


    while True:
        try:
            num=int(input("Enter a number: \n"))    
            break  # Break out of the loop if an integer value is entered
        except ValueError:
            print("Invalid input. Please enter an integer.")
    print("\n")


    if num==1:
        @app.route("/create_player", methods=["POST"])
        def handle_create_player():
            create_player()

    elif num==2:
        @app.route('/Average',methods=['GET'])
        def handle_average():
            calc_average()

    elif num==3:
        @app.route('/make_team', methods=['GET'])
        def handle_team_select():
            team_select()
    elif num==4:
        @app.route('/random_select', methods=['GET'])
        def handle_rand_select():
            rand_select()
    elif num==5:
        @app.route('/count',methods=['GET'])
        def handle_pos_count():
            pos_count()
    elif num==6:
        @app.route('/sort_apt', methods=['GET'])
        def handle_APT_sort():
            APT_sort()
    elif num==7:
        @app.route('/highest_APT', methods=['GET'])
        def handle_highest_APT():
            highest_APT()
    elif num==8:
        @app.route('/lowest_avg',methods=['GET'])
        def handle_lowest_AVG():
            lowest_AVG()

