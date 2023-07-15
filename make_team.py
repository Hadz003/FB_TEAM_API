from flask import jsonify, request

import mysql.connector

host = '127.0.0.1'  
user = 'root'  
password = 'Kansas16'  
database = 'fb_team_database'  

def team_select():
    conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database)
    cursor=conn.cursor()
    query=''' Select * 
            FROM players'''
    cursor.execute(query)
    result=cursor.fetchall()
    conn.close()
    cursor.close()

    if len(result)<10:
        return ("Not enough players available, please input more players to build a team"),400
    data=request.json
    num_of_def=data.get('num_of_def')
    num_of_mid=data.get('num_of_mid')
    num_of_attack=data.get('num_of_attack')

    conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database)
    cursor=conn.cursor()
    return_player_query='''
                            SELECT *
                            FROM players
                            WHERE position_=%s
                        '''
    cursor.execute(return_player_query,["Attacker"])
    Attackers=cursor.fetchall()
    conn.close()
    cursor.close()
    conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database)
    cursor=conn.cursor()
    return_player_query='''
                            SELECT *
                            FROM players
                            WHERE position_=%s
                        '''
    cursor.execute(return_player_query,["Defender"])
    Defenders=cursor.fetchall()
    
    conn.close()
    cursor.close()
    conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database)
    cursor=conn.cursor()
    return_player_query='''
                            SELECT *
                            FROM players
                            WHERE position_=%s
                        '''
    cursor.execute(return_player_query,["Midfielder"])
    Midfielders=cursor.fetchall()
    conn.close()
    cursor.close()

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
        return("not 10 players"),404
    sorted_defence=sorted( Defenders, key=lambda player: player[4], reverse=True)
    sorted_mid=sorted( Midfielders, key=lambda player: player[4], reverse=True)
    sorted_attack=sorted( Attackers, key=lambda player: player[4], reverse=True)

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
    dict={}
    for playe in team:
        nam="player_"+str(playe[0])
        dict[nam]=str(playe[1])
        print(dict[nam])
    return jsonify({"Team":dict})