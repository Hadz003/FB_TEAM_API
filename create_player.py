from flask import Flask, jsonify, request
from arrays import players,Defenders,Attackers,Midfielders


i_d = 1


class player(object):
    def __init__(self, ID, first_name, last_name, APT, SET, nationality, position):
        self.first_name = first_name
        self.last_name = last_name
        self.APT = APT
        self.SET = SET
        self.position = position
        self.nationality = nationality
        self.ID = ID

    def __str__(self):
        return (
            str(self.ID)
            + " "
            + self.first_name
            + " "
            + self.last_name
            + " "
            + str(self.APT)
            + " "
            + str(self.SET)
            + " "
            + self.nationality
            + " "
            + self.position
        )



def create_player():
    global i_d
    if request.method=="POST":

        first_name= request.form['first_name']
        last_name= request.form['last_name']
        apt= request.form['APT']
        set_value= request.form['SET']
        nationality= request.form['nationality']
        position= request.form['position']

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
        for i in players:
            if i.first_name==new_player.first_name and i.last_name==new_player.last_name:
                return("Player already added")
        players.append(new_player)
        i_d += 1

        if position == "Defender":
            Defenders.append(new_player)
            Defenders.sort(key=lambda player: player.SET, reverse=True)
        elif position == "Midfielder":
            Midfielders.append(new_player)
            Midfielders.sort(key=lambda player: player.SET, reverse=True)
        else:
            Attackers.append(new_player)
            Attackers.sort(key=lambda player: player.SET, reverse=True)
        return jsonify({"message": "Player created successfully", "player": str(new_player)}), 201


    else:
        return jsonify({'error':'invalid request'})
