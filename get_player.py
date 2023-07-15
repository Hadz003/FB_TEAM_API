from flask import jsonify,request
import mysql.connector

host = '127.0.0.1'  
user = 'root'  
password = 'Kansas16'  
database = 'fb_team_database'  

def get_player():
    data=request.json
    i_d=data.get("id")
    try:
        i_d = int(i_d)
        if i_d < 0:
            raise ValueError
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid i_d."}), 400
    conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    cursor = conn.cursor()
    select_='''SELECT * FROM players'''
    cursor.execute(select_)
    check=cursor.fetchall()
    if len(check)<i_d:
        return jsonify({"Error":"There is no player with this id"}),404

    cursor.close()
    conn.close
    conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database)
    cursor=conn.cursor()
    return_player_query='''
                            SELECT *
                            FROM players
                            WHERE id=%s
                        '''
    cursor.execute(return_player_query,(i_d,))
    execute_player=cursor.fetchall()
    conn.close()
    cursor.close()

    res_str="id:{} firstname: {} last_name: {}".format(execute_player[0][0], execute_player[0][1],execute_player[0][2])
    return jsonify({"Player":str(res_str)}), 200
