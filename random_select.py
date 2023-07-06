from arrays import (players)
from flask import Flask, jsonify, request
import random


def rand_select():
    rand_num=request.form['rand_num']  
    try:
        rand_num=int(rand_num)
        if rand_num>len(players) or rand_num<0:
            raise ValueError
    except (ValueError,TypeError):
        return jsonify({'error':"Invalid input. Enter a number less than "+ str(len(players))})


    rand_list=random.sample(players,rand_num)
    string=''
    for i in rand_list:
        string=string+str(i)+" \n"
    return (string)
