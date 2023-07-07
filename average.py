from arrays import players
from flask import Flask, jsonify, request

def Average(player):
    return float((player.APT +player.SET)/2)

def calc_average():
    found=False
    data=request.json
    find_by_name=data.get('find_by_name')
    find_by_last_name=data.get('find_by_last_name')

    if not isinstance(find_by_name, str) or find_by_name.isdigit()==True or not find_by_name:
        return jsonify({"error": "Invalid first name"}), 400
    
    if not isinstance(find_by_last_name, str) or find_by_last_name.isdigit()==True or not find_by_last_name:
        return jsonify({"error": "Invalid last name"}), 400
    for i in players:
        if i.first_name==find_by_name and i.last_name==find_by_last_name :
            found=True
            found_player=i
            break
    if found==True:
        return jsonify({'Average':"The Average of "+ str(find_by_name) +" "+ str(find_by_last_name)+ " is : "+ str(Average(found_player))})
    else:
        return jsonify("Player Not Found")
