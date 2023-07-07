from arrays import (players)
from flask import jsonify, request
import random


def rand_select():
    data=request.json
    rand_num=data.get('rand_num')
    try:
        rand_num=int(rand_num)
        if rand_num>len(players) or rand_num<0:
            raise ValueError
    except (ValueError,TypeError):
        return jsonify({'error':"Invalid input. Enter a number less than "+ str(len(players))})


    rand_list=random.sample(players,rand_num)
    dict={}
    for playe in rand_list:
        nam="player_"+str(playe.ID)
        dict[nam]=str(playe.first_name)
        print(dict[nam])
    return jsonify({"random_player_names":dict})

