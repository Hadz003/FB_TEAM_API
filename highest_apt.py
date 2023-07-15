from flask import jsonify
import mysql.connector

host = '127.0.0.1'  
user = 'root'  
password = 'Kansas16'  
database = 'fb_team_database'  

def highest_APT():
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
    res_str="id:{} firstname: {} last_name: {} apt: {}".format(result[0][0], result[0][1],result[0][2], result[0][3])
    cursor.close()
    conn.close()
    return jsonify({"Highest_apt": str(res_str)}),200