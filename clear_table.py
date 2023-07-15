from flask import jsonify,request
import mysql.connector
from auto_increment import auto_increment
host = '127.0.0.1' 
user = 'root' 
password = 'Kansas16'  
database = 'fb_team_database'  

def clear_table_():
    conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    cursor = conn.cursor()
    select_query='''SELECT * FROM players'''
    cursor.execute(select_query)
    check=cursor.fetchall()
    if len(check)<1:
        auto_increment()
        return jsonify({"Error":"Table is already clear"}),404

    cursor.close()
    conn.close

    conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    cursor = conn.cursor()

    delete_query='''DELETE FROM players'''
    
    cursor.execute(delete_query)

    conn.commit()
    cursor.close()
    conn.close()
    auto_increment()
    return jsonify({"Message": "Table cleared"}),200

