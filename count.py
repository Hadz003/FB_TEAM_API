from arrays import (Defenders,Attackers,Midfielders)
from flask import Flask, jsonify, request



def pos_count():
    return jsonify({"Attackers": str(len(Attackers)) , "Midfielders":str(len(Midfielders)), "Defenders": str(len(Defenders))})
