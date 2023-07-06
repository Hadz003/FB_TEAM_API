from arrays import (players,Defenders,Attackers,Midfielders)
from flask import Flask, jsonify, request
import random

def team_select():

    if len(players)<10:
        return ("Not enough players available, please input more players to build a team")

    num_of_def=request.form['num_of_def']
    num_of_mid=request.form['num_of_mid']
    num_of_attack=request.form['num_of_attack']


    try:
        num_of_def=int(num_of_def)
        if num_of_def>len(Defenders):
            raise ValueError
    except (ValueError,TypeError):
        return jsonify({"error": "Invalid input Please enter " +str(len(Defenders)) +" or less Defenders"}), 400

    try:
        num_of_mid=int(num_of_mid)
        if num_of_mid>len(Midfielders):
            raise ValueError
    except (ValueError,TypeError):
        return jsonify({"error": "Invalid input. Please enter "+ str(len(Midfielders))+ " or less Defenders"}), 400

    try:
        num_of_attack=int(num_of_attack)
        if num_of_attack>len(Attackers):
            raise ValueError
    except (ValueError,TypeError):
        return jsonify({"error": "Invalid input. Please enter "+ str(len(Attackers))+ " or less Defenders"}), 400
    
    if (num_of_attack + num_of_def + num_of_mid)!=10:
        return("not 10 players")
    sorted_defence=sorted( Defenders, key=lambda player: player.SET, reverse=True)
    sorted_mid=sorted( Midfielders, key=lambda player: player.SET, reverse=True)
    sorted_attack=sorted( Attackers, key=lambda player: player.SET, reverse=True)

    defence=[0]*num_of_def
    midfield=[0]*num_of_mid
    attack=[0]*num_of_attack

    for i in range(num_of_def):
        defence[i]=sorted_defence[i]
    for i in range(num_of_mid):
        midfield[i]=sorted_mid[i]
    for i in range(num_of_attack):
        attack[i]=sorted_attack[i]


    team = defence + attack + midfield
    string_3=''
    for i in team:
        string_3=string_3+str(i)+" \n"
    return (string_3)