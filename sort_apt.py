from arrays import players
from flask import Flask, jsonify, request


def APT_sort():
    sorted_by_apt=sorted( players, key=lambda player: player.APT, reverse=True)
    dict={}
    for playe in sorted_by_apt:
        nam="player_"+str(playe.ID)
        dict[nam]=str(playe.first_name)
        print(dict[nam])
    return jsonify({"sorted players by apt":dict})
    