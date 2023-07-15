from flask import jsonify
import mysql.connector

host = '127.0.0.1'  
user = 'root'  
password = 'Kansas16'  
database = 'fb_team_database'  

def lowest_AVG():
    conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database)
    cursor=conn.cursor()
    lowest_average_query=''' Select * 
                          FROM players
                          ORDER BY Average ASC 
                          '''
    cursor.execute(lowest_average_query)
    result=cursor.fetchall()
    res_str="id:{} firstname: {} last_name: {} average: {}".format(result[0][0], result[0][1],result[0][2], result[0][-1])
    cursor.close()
    conn.close()
    return jsonify({"Lowest Average": str(res_str)}),200