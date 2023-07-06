#1 & #2
#We create a class to define a player's characteristics
class player(object):
    def __init__ (self,I_D,first_name,last_name,APT,SET,nationality,position):
        self.first_name=first_name
        self.last_name=last_name
        self.APT=APT
        self.SET=SET
        self.position=position
        self.nationality=nationality
        self.I_D=I_D
    def __str__(self):
        return str(self.I_D) + " " + self.first_name + " " + self.last_name + " " + str(self.APT) + " " + str(self.SET) + " " + self.nationality + " " + self.position
#################################################################################################
#2
def Average(player):
    return float((player.APT +player.SET)/2)
players=[]

Defenders=[]
Midfielders=[]
Attackers=[]

#############################################################################################################


#3
#user input to make a team
def team_select():
    check=True
    if len(players)<10:
        print("Not enough players available, please input more players to build a team")
        check=False
    while check==True:
        while True:
            try:
                num_of_def=int(input("Enter the number of defenders: "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
        while True:
            try:
                num_of_mid=int(input("Enter the number of midfielders: "))
                break
            except:
                print("Invalid input. Please enter an integer.")
        while True:
            try:
                num_of_attack=int(input("Enter the number of attackers: "))
                break
            except:
                print("Invalid input. Please enter an integer.")


        if (num_of_attack + num_of_def + num_of_mid)!=10:
            print("not 10 players")
            continue

        if num_of_def>len(Defenders):
            print("Not enough defenders available")
            continue
        if num_of_mid>len(Midfielders):
            print("Not enough midfielders available")
            continue
        if num_of_attack>len(Attackers):
            print("Not enough attackers available")
            continue
        check=False
        #print("ID First Name Last Name APT SET Nationality Position")
        for i in range(num_of_def):
            print(Defenders[i])
        for i in range(num_of_mid):
            print(Midfielders[i])
        for i in range(num_of_attack):
            print(Attackers[i])
#################################################################################################################

#4
#random select players according to user input

def rand_select():
    check=True
    while check==True:
        while True:
            try:
                rand_num=int(input("Enter the number of players required: "))
                break
            except:
                print("Invalid input. Please enter an integer.")

        if rand_num>len(players):
            print("Not enough players available, thereare only "+str(len(players))+" players")
            continue
        elif rand_num<0:
            print("Very few players!")
            continue
        check=False
        import random
        #now we sample
        #print("ID First Name Last Name APT SET Nationality Position") 
        rand_list=random.sample(players,rand_num)

        for i in rand_list:
            print(i)
##################################################################################################################

#5
#counting players based on position
def pos_count():
    print("Attackers: "+str(len(Attackers)))
    print("Midfielders: "+str(len(Midfielders)))
    print("Defenders: "+str(len(Defenders)))
#####################################################################################################################

#6
#sort all players by APT from high to low 
def APT_sort():
    print("ID First Name Last Name APT SET Nationality Position")
    x=sorted( players, key=lambda player: player.APT, reverse=True)
    for i in x:
        print(i)
####################################################################################################################

#7
#Find the player with the highest APT score
def highest_APT():
    print("ID First Name Last Name APT SET Nationality Position")
    l=sorted(players, key=lambda player: player.APT, reverse=True)
    print(l[0])
#####################################################################################################################
#8
#Find the player with lowest AVG score
def lowest_AVG():
    counter=100
    found="None"
    for i in range(len(players)):
        if Average(players[i])<counter:
            counter=Average(players[i])
            found=str(players[i])
    #print("ID First Name Last Name APT SET Nationality Position")
    print (found)
print("Welcome to the Football Team Program!!\n")
num=1
i_d=1
while num !=0:

    print("\nChoose one of the options below:\n\n1. Create a new player\n2. Get a player's average\n3. Make a team of 10 players\n4. Randomly select players\n5. Count players based on position\n6. Sort all players by APT from high to low\n7. Find the player with the highest APT score\n8. Find the player with lowest AVG score\n\nPress 0 to exit the program ")
    while True:
        try:
            num=int(input("Enter a number: "))    
            break  # Break out of the loop if an integer value is entered
        except ValueError:
            print("Invalid input. Please enter an integer.")
    print("\n")
    if num==1:

        first_name = input("Enter the player's first name: ")
        while not isinstance(first_name, str) or first_name.isdigit()==True:
            print("Invalid input. Please enter a string.")
            first_name = input("Enter the player's first name: ")

        last_name=input("Enter the player's last name: ")
        while not isinstance(last_name, str) or last_name.isdigit()==True:
            print("Invalid input. Please enter a string.")
            last_name=input("Enter the player's last name: ")

        while True:
            try:
                apt = int(input("Enter the player's APT: "))
                if apt>100 or apt<0 :
                    continue
                break  # Break out of the loop if an integer value is entered
            except ValueError:
                print("Invalid input. Please enter an integer.")

        while True:
            try:
                set=int(input("Enter the player's SET: "))
                if set>100 or set<0 :
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

        na=input("Enter the player's Nationality: ")
        while not isinstance(na, str):
            print("Invalid input. Please enter a string.")
            na=input("Enter the player's Nationality: ")
        while True:
            if na=="Scotland":
                break
            elif na=="England":
                break
            elif na=="Northern Ireland":
                break
            elif na=="Wales":
                break
            else:
                print("Invalid Country")
                na=input("Enter the player's Nationality: ")

        Position=input("Enter the player's position: ")
        while not isinstance(Position, str):
            print("Invalid input. Please enter a string.")
            Position=input("Enter the player's position: ")
        while True:
            if Position=="Defender":
                break
            elif Position=="Midfielder":
                break
            elif Position=="Attacker":
                break
            else:
                print("Invalid position")
                Position=input("Enter the player's position: ")
        

        x=player(i_d,first_name,last_name,apt,set,na,Position)

        if x.position=="Defender":
            Defenders.append(x)
            Defenders.sort(key= lambda player: player.SET, reverse=True)
        elif x.position=="Midfielder":
            Midfielders.append(x)
            Midfielders.sort(key= lambda player: player.SET, reverse=True)
        else :
            Attackers.append(x)
            Attackers.sort(key= lambda player: player.SET, reverse=True)

        players.append(player(i_d,first_name,last_name,apt,set,na,Position))
        i_d=i_d + 1

    elif num==2:
        found=False
        find_by_name=input("Enter the first_name of the player: ")
        while not isinstance(find_by_name, str) or find_by_name.isdigit()==True:
            print("Invalid input. Please enter a string.")
            find_by_name=input("Enter the first_name of the player: ")
        find_by_last_name=input("Enter the last_name of the player: ")
        while not isinstance(find_by_last_name, str) or find_by_last_name.isdigit()==True:
            print("Invalid input. Please enter a string.")
            find_by_last_name=input("Enter the last_name of the player: ")
        for i in players:
            if i.first_name==find_by_name  and i.last_name==find_by_last_name :
                found=True
                found_player=i
                break
        if found==True:
            print("\nThe Average of "+find_by_name+" "+find_by_last_name+" is "+str(Average(found_player)))
        else:
            print("player not found")

    elif num==3:
       team_select()
    elif num==4:
        rand_select()
    elif num==5:
        pos_count()
    elif num==6:
        APT_sort()
    elif num==7:
        highest_APT()
    elif num==8:
        lowest_AVG()

print("GoodBye!")


