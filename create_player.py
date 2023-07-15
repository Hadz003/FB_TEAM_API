from flask import jsonify, request
import mysql.connector

host = '127.0.0.1' 
user = 'root' 
password = 'Kansas16'  
database = 'fb_team_database'  

class player(object):
    def __init__(self, ID, first_name, last_name, APT, SET, nationality, position):
        self.first_name = first_name
        self.last_name = last_name
        self.APT = APT
        self.SET = SET
        self.position = position
        self.nationality = nationality
        self.ID = ID

    def to_dict(self):
        return {
            "ID": str(self.ID),
            "first_name": self.first_name,
            "last_name": self.last_name,
            "apt": str(self.APT),
            "set": str(self.SET),
            "nationality": self.nationality,
            "position": self.position
        }

    def __str__(self):
        return str(self.to_dict())


def create_player():
    global i_d
    if request.method=="POST":
        data=request.json
        first_name= data.get('first_name')
        last_name= data.get('last_name')
        apt= data.get('APT')
        set_value= data.get('SET')
        nationality= data.get('nationality')
        position= data.get('position')

        if not isinstance(first_name, str) or first_name.isdigit() or not first_name:
            return jsonify({"error": "Invalid first name"}), 400

        if not isinstance(last_name, str) or last_name.isdigit() or not last_name:
            return jsonify({"error": "Invalid last name"}), 400
        try:
            apt = int(apt)
            if apt < 0 or apt > 100:
                raise ValueError
        except (ValueError, TypeError):
            return jsonify({"error": "Invalid APT. Please enter an integer between 0 and 100."}), 400

        try:
            set_value = int(set_value)
            if set_value < 0 or set_value > 100:
                raise ValueError
        except (ValueError, TypeError):
            return jsonify({"error": "Invalid SET. Please enter an integer between 0 and 100."}), 400
        if not isinstance(nationality, str) or not nationality:
            return jsonify({"error": "Invalid nationality"}), 400

        valid_nationalities = ["Scotland", "England", "Northern Ireland", "Wales"]
        if nationality not in valid_nationalities:
            return jsonify({"error": "Invalid nationality. Please choose from Scotland, England, Northern Ireland, Wales."}), 400

        if not isinstance(position, str) or not position:
            return jsonify({"error": "Invalid position"}), 400

        valid_positions = ["Defender", "Midfielder", "Attacker"]
        if position not in valid_positions:
            return jsonify({"error": "Invalid position. Please choose from Defender, Midfielder, Attacker."}), 400
        new_player = player(i_d, first_name, last_name, apt, set_value, nationality, position)
        
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = conn.cursor()

        select_query = '''
        SELECT * 
        FROM players 
        WHERE first_name = %s AND last_name = %s AND apt = %s AND set_ = %s AND position_ = %s AND nationality = %s
        '''
        cursor.execute(select_query, (new_player.first_name, new_player.last_name, new_player.APT, new_player.SET, new_player.position, new_player.nationality))

        result = cursor.fetchall()

        player_exists = len(result) > 0
        if player_exists==True:
            return jsonify({"Exists":"Player Already Added"}),200
        cursor.close()
        conn.close()

        if player_exists==False:
            conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database)
            cursor=conn.cursor()

            insert_query='''
            INSERT INTO players (first_name, last_name, apt, set_, position_, nationality)
            VALUES (%s, %s, %s, %s, %s, %s)
            '''
            cursor.execute(insert_query, (new_player.first_name, new_player.last_name, new_player.APT, new_player.SET, new_player.position, new_player.nationality))
            conn.commit()
            last_row=cursor.lastrowid
            cursor.close()
            conn.close()
  
        conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database)
        cursor=conn.cursor()
        return_player_query='''SELECT *
                               FROM players
                               WHERE id=%s
                                 '''
        cursor.execute(return_player_query,[last_row])
        execute_player=cursor.fetchall()
        conn.close()
        cursor.close()
        res_str="id:{} firstname: {} last_name: {}".format(execute_player[0][0], execute_player[0][1],execute_player[0][2])
        return jsonify({"message": "Player created successfully", "Player":str(res_str)}), 201


    else:
        return jsonify({'error':'invalid request'}),400
