from flask import jsonify
import mysql.connector

host = '127.0.0.1' 
user = 'root' 
password = 'Kansas16'  
database = 'fb_team_database'  


def pos_count():
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
    return jsonify({"Attackers": str(len(Attackers)) , "Midfielders":str(len(Midfielders)), "Defenders": str(len(Defenders))})
