import random
import os
import sys
#sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=32, cols=100))

#Global Variables


class GlobalVariables:
    def __init__(self):
        self.location = "Room"
        self.time = 800
        # format : 800 8 am 1230 12:30 pm

    def time_change(self, number):
        if int(str(self.time)[-2:]) + number >= 60:
            hour = (int(str(self.time)[-2:]) + number) // 60
            self.time += hour * 100 - number
            #self.time += hour * 100 + int(str(self.time)[-2:]) - (int(str(self.time)[-2:]) + number)
        else:
            self.time += number
        print("current time: {0} : {1}".format(str(self.time)[:-2],str(self.time)[-2:]))
        return self.time
    
    def sanity_change(self, sanity, number):
        sanity += number
        return sanity
    
    def sanity_check(self, sanity):
        if sanity < 80:
            print('you feel a bit uneasy')
        if sanity < 50:
            print('You begin to question if everything until this point is normal.')

class Player:
    def __init__(self, name):
        self.name = name
        self.hunger_level = 50
        self.money = 50
        self.sanity = 100
        self.death = False

    def hungerDeath(self):
            if hunger_level <= 0:
                print('You died of hunger.')
                self.death = True
                return self.death

class Location(Player):
    def __init__(self):
        self.action = 0
        self.where = "Room"
        self.first_time = True

    def check_bedroom(self):
        if self.first_time:
            print("You looked around your room. There's your bed, your pet snake Monty's tank, and your desk.")
            self.first_time = False
        else:
            print("You are back at the center of your room.")
        self.action = input("""
        pick an action:
        [1]check desk       [4]go to kitchen/living room
        [2]check bed        [5]"..."
        [3]check tank       [6]"......"
        """)
        self.action = int(self.action)
        if self.action == 1:
            return self.desk()
        elif self.action == 2:
            return self.bed()
        elif self.action == 3:
            return self.tank()
        elif self.action == 4:
            print("you moved to the kitchen/living room")
        elif self.action == 5:
            print("you stared at the ceiling.")
            event.time_change(15)
            return self.check_bedroom()
        elif self.action == 6:
            print("you stare intensively at the ceiling,reflecting on your life")
            event.time_change(30)
            return self.check_bedroom()
        else:
            print('please enter a valid response')
            return self.check_bedroom()

    def desk(self):
        print("Your computer is on. It's on almost 24/7.")
        action = input("""
        pick an action:
        [1]check social media        [4]walk away
        [2]check news                [5]"..."
        [3]check message board       [6]"......"
        """)
        action = int(action)
        if action == 1:
            pass
        elif action == 2:
            pass
        elif action == 3:
            pass
        elif action == 4:
            return self.check_bedroom()
        elif action == 5:
            print("you stared at the ceiling.")
            event.time_change(15)
            return self.desk()
        elif action == 6:
            print("you stare intensively at the ceiling,reflecting on your life")
            event.time_change(30)
            return self.desk()
        else:
            print('please enter a valid response')
            return self.desk()

    def bed(self):
        print("Your bed is messy. You should probably make your bed.")
        action = input("""
        pick an action:
        [1]sleep                  [3]"..."
        [2]make bed               [4]"......"
        """)
        if action == '1':
            #return sleep()
            pass
        elif action == '2':
            #return make_bed()
            pass
        elif action == '3':
            print('you stare at your bed')
            event.time_change(15)
        elif action == '4':
            print('You stare at your bed intensively.')
            event.time_change(30)

    def tank(self):
        print("You look at the tank.")
        self.action = input("""
        pick an action:
        [1]check social media        [4]walk away
        [2]check news                [5]"..."
        [3]check message board       [6]"......"
        """)


#For terminal
clear = lambda: os.system('cls')
width, height = os.get_terminal_size()


#Gameplay starts here
clear()

print("""

    ------------------------------------------------------------
        You Woke Up In Your Room On A Staturday Morning
    ------------------------------------------------------------


""")

name = input("Name your character:\n")

# initialization
player = Player(name)
location = Location()
event = GlobalVariables()

name_confirm = input('Your character name is {0}, right? (Y/N) '.format(player.name)).upper()
while name_confirm == 'N':
    player.name = input("Name your character ")
    name_confirm = input('Your character name is {0}, right? (Y/N)'.format(player.name)).upper()
clear()
print("""
You woke up in your room.
It's currently early morning on a Saturday. Your stomach rumbles. It's time for breakfast.... Well, only if you didn't run out of food. You probably should stay on top of your grocery shopping.
So it's time to go get some food, and probably grocery as well.
It's time to step on a journey. A joureny to the grocery store.
""")
location.check_bedroom()

x = input('current testing ends.press enter to exit.')