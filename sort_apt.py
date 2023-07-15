from flask import jsonify
import mysql.connector

host = '127.0.0.1'  
user = 'root'  
password = 'Kansas16'  
database = 'fb_team_database'  
def APT_sort():
    conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database)
    cursor=conn.cursor()
    highest_apt_query=''' Select * 
                          FROM players
                          ORDER BY apt DESC 
                          '''
    cursor.execute(highest_apt_query)
    result=cursor.fetchall()
    return jsonify({"sorted players by apt":result})
    