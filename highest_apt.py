from arrays import players
from flask import Flask, jsonify, request


def highest_APT():
    l=sorted(players, key=lambda player: player.APT, reverse=True)
    return jsonify({"Highest_apt": str(l[0])})