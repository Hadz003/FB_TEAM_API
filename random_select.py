
from flask import jsonify, request
import random
import mysql.connector

host = '127.0.0.1' 
user = 'root'  
password = 'Kansas16'  
database = 'fb_team_database'  

def rand_select():
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
    data=request.json
    rand_num=data.get('rand_num')
    try:
        rand_num=int(rand_num)
        if rand_num>len(result) or rand_num<0:
            raise ValueError
    except (ValueError,TypeError):
        return jsonify({'error':"Invalid input. Enter a number less than "+ str(len(result))})


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

    rand_list=random.sample(result,rand_num)
    conn.close()
    cursor.close()
    return jsonify({"random_player_names":rand_list})

