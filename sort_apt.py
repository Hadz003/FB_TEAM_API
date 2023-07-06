from arrays import players
from flask import Flask, jsonify, request


def APT_sort():
    sorted_by_apt=sorted( players, key=lambda player: player.APT, reverse=True)
    string_2=''
    for i in sorted_by_apt:
        string_2=string_2+str(i)+" \n"
    return (string_2)
    
    