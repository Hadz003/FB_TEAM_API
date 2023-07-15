from flask import jsonify,request
import mysql.connector

host = '127.0.0.1' 
user = 'root' 
password = 'Kansas16'  
database = 'fb_team_database'  

def delete_player_():
    data=request.json
    i_d=data.get('id')

    conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    cursor = conn.cursor()

    delete_query='''DELETE FROM players
                    WHERE id = %s'''
    
    cursor.execute(delete_query, (i_d,))

    conn.commit()
    cursor.close()
    conn.close()


    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    cursor = conn.cursor()

    select_query = '''SELECT id 
                      FROM players 
                      ORDER BY id'''
    
    cursor.execute(select_query)
    players = cursor.fetchall()
    print(players)

    for index, player in enumerate(players, start=1):
        update_query = '''UPDATE players 
                          SET id = %s 
                          WHERE id = %s'''
        cursor.execute(update_query, (index, player[0]))

    conn.commit()

    cursor.close()
    conn.close()


    return jsonify({"Delete message":"Player Deleted Successfullly"}),200
