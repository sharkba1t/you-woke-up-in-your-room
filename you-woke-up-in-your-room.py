import random
import os
import sys
#sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=32, cols=100))

#For terminal
clear = lambda: os.system('cls')
width, height = os.get_terminal_size()

#Global Variables


class GlobalVariables:
    def __init__(self):
        self.location = "Room"
        self.time = 800
        # format : 800 8 am 1230 12:30 pm

    def time_change(self, number):
        if (int(str(self.time)[-2:]) + number >= 60) and (number < 60):
            hour = (int(str(self.time)[-2:]) + number) // 60
            self.time += hour * 100 - number
            #self.time += hour * 100 + int(str(self.time)[-2:]) - (int(str(self.time)[-2:]) + number)
        elif number == 60:
            self.time += 100
        else:
            self.time += number
        print("current time: {0} : {1}".format(str(self.time)[:-2],str(self.time)[-2:]))
        if 800 <= self.time < 1200:
            print("It's currently morning.")
        elif 1200 <= self.time < 1300:
            print("It's currently noon.")
        elif 1300 <= self.time < 1700:
            print("It's currently afternoon.")
        elif 1700 <= self.time < 1900:
            print("It's currently evening. The grocery store will close at 21:00.")
        return self.time

    def hunger_change(self, hunger_level, hunger):
        if hunger < 0:
            hunger_level += hunger
            print("Your stomach rumbles a bit.")
        if hunger > 0:
            hunger_level += hunger
            print("You feel less hungry now.")
        return hunger_level


    def sanity_check(self, sanity, number):
        sanity += number
        if sanity < 80:
            print('you feel a bit uneasy')
        if sanity < 50:
            print('You begin to question if everything until this point is normal.')
        return sanity
    
    def invalid_input(self):
        print('please enter a valid response')

class Player:
    def __init__(self, name):
        self.name = name
        self.hunger_level = 50
        self.money = 50
        self.sanity = 100
        self.death = False
        self.carrying_monty = False
        self.death = False
        self.morning_routine = False

    def hunger_death(self):
            if hunger_level <= 0:
                print('You died of hunger.')
                self.death = True
                return self.death

    def sanity_death(self):
        self.death = True
        return self.death

class Location:
    def __init__(self):
        pass

class Apartment:
    def __init__(self):
        self.first_time_bedroom = True
        self.first_time_kitchen = True
        self.first_time_check_fridge = True
        self.bed_is_messy = True
        self.check_freezer = False
        self.ate_mice = False

#Main actions - Bedroom
    def check_bedroom(self):
        if self.first_time_bedroom:
            print("You looked around your room. There's your bed, your pet snake Monty's tank, and your desk.")
            self.first_time = False
        else:
            print("You are back at the center of your room.")
            print("===============================")
        action = input("""
    pick an action:
    [1]check desk       [4]go to kitchen/living room
    [2]check bed        [5]"..."
    [3]check tank       [6]"......"
    """)
        action = int(action)
        if action == 1:
            return self.desk()
        elif action == 2:
            return self.bed()
        elif action == 3:
            return self.tank()
        elif action == 4:
            print("you moved to the kitchen/living room")
            return self.check_kitchen()
        elif action == 5:
            print("you gazed at the ceiling.")
            event.time_change(15)
            return self.check_bedroom()
        elif action == 6:
            print("you stare intensively at the ceiling,reflecting on your life.")
            event.time_change(30)
            return self.check_bedroom()
        else:
            event.invalid_input()
            return self.check_bedroom()

# specific areas

    def desk(self):
        print("Your computer is on. It's on almost 24/7. Other than that, nothing else caught your attention here.")
        return self.check_bedroom()

    def bed(self):
        if self.bed_is_messy:
            print("Your bed is messy. You should probably make your bed.")
        else:
            print("Your bed is now tidy.")
        action = input("""
        pick an action:
        [1]sleep                  [4]"..."
        [2]make bed               [5]"......"
        [3]walk away
        """)
        if action == '1':
            print("Screw responsibilities. it's time for a nap,")
            event.time_change(60)
            self.bed_is_messy = True
            return self.bed()
        elif action == '2':
            if self.bed_is_messy:
                print("You made your bed. It is tidy now.")
                self.bed_is_messy = False
                event.time_change(15)
                return self.bed() 
            else:
                print("Your already made your bed.")
                return self.bed()
        elif action == '3':
                print("You walked away form your bed.")
                return self.check_bedroom() 
        elif action == '4':
            print('you gaze at your bed. This is where you sleep every night.')
            event.time_change(15)
            return self.bed()
        elif action == '5':
            print('You stare at your bed intensively. You are lost in your thoughts.')
            event.time_change(30)
            return self.bed()
        else:
            event.invalid_input()
            return self.bed()

    def tank(self):
        if not player.carrying_monty:
            print("You looked at the tank. Your pet snake, Monty, a ball python, is napping in its hide.")
            action = input("""
    pick an action:
    [1]take Monty out of the tank        [3]"..."
    [2]walk away                         [4]"......"
        """)
        else:
            print("Monty is now resting on your arm.")
            print("Monty: pssssssst.")
            action = input("""
    pick an action:
    [1]put Monty back in the tank        [3]"..."
    [2]walk away                         [4]"......"
        """)
        if action == '1':
            if player.carrying_monty:
                print("Monty: psssssssst")
                print("You put Monty back in its tank.")
                player.carrying_monty = False
            else:
                print("you took Monty out of its hide. It climbs on your arm.")
                print("Monty: psssst")
                player.carrying_monty = True
            event.time_change(5)            
            return self.tank()
        elif action == '2':
            if player.carrying_monty:
                print("Monty: psssssssst")
                print("It's probably a bad idea to carry Monty with you right now.")
                return self.tank()
            else:
                print("You left Monty alone for now.")
                return self.check_bedroom() 
        elif action == '3':
            if player.carrying_monty:
                print("Monty: psssssssst")
                print("You gaze at Monty. It rests on your arm and seems content.")
            else:
                print("You gaze at the tank. Monty is napping.")
            event.time_change(15)
            return self.tank()
        elif action == '4':
            if player.carrying_monty:
                print("Monty: psssssssst")
                print("You start a staring contest with Monty.")
                print("......")
                print("Your eyes hurt from staring. You blink to moisturize your eyes.")
                print("Monty won the staring contest. It can't blink, afterall.")
            else:
                print("You stare at the tank. Monty does not seem to be bothered by you at all.")
            event.time_change(30)
            return self.tank()
        else:
            event.invalid_input()
            return self.tank()

#Main actions - Kitchen
    def check_kitchen(self):
        if self.first_time_kitchen:
            print("You are now in your kitchen/living room. The bathroom is to your right- that's also where you do half of your morning routine. The apartment door is in the front.")
            self.first_time_kitchen = False
        else:
            print("You are now in your kitchen/living room.")
        action = input("""
    pick an action:
    [1]check the fridge               [4]leave apartment
    [2]go to bathroom                 [5]"..."
    [3]go to bedroom                  [6]"......"
        """)
        if action == '1':
            return self.fridge()
        elif action == '2':
            return self.bathroom()
        elif action == '3':
            return self.check_bedroom()
        elif action == '4':
            return self.leave_apartment()
        elif action == '5':
            print('You stand in your kitchen and space out a bit.')
            event.time_change(15)
            return self.check_kitchen()
        elif action == '6':
            print('You stare into the nothingness for quite a while.')
            event.time_change(30)
            return self.check_kitchen()
        else:
            event.invalid_input()
            return self.check_kitchen()

    def bathroom(self):
        print("You are in the bathroom.")
        action = input("""
    pick an action:
    [1]Get ready for the day            [3]"..."
    [2]Go to kitchen/living room        [4]"......"
        """)
        action = int(action)
        if action == 1:
            if not player.morning_routine:
                print("......")
                print("You finished your morning routine. You are ready to leave your apartment now.")
                player.morning_routine = True
            else: 
                print("You've already done that. It is now time for grocery shopping.")
            return self.bathroom()
        elif action == 2:
            print("you returned to the kitchen.") 
            return self.check_kitchen()
        elif action == 3:
            print("You gaze at the mirror. Do you always look like that?")
            event.time_change(15)
            return self.bathroom()
        elif action == 4:
            print("You stare at your reflection in the mirror. You almost forgot why you are here. ")
            event.time_change(30)
            return self.bathroom()
        else:
            event.invalid_input()
            return self.bathroom()


# Sub Spaces for Kitchen Area
    def fridge(self):
        if self.first_time_check_fridge:
            print("""You opened the fridge door. There are a few soda cans left here, but other than that, there is nothing to eat here. Maybe there's still frozen food left in your freezer?""")
            self.first_time_check_fridge = False
        elif self.ate_mice:
            print("Your fridge is now out of food, including snake food.")
        else:
            print("You stand in front of your fridge, a fridge without any human food.")
        action = input("""
    pick an action:
    [1]check freezer               [3]"..."
    [2]walk away                   [4]"......"
        """)
        if action == '1':
            self.freezer()
            return self.fridge()
        elif action == '2':
            return self.check_kitchen()
        elif action == '3':
            print('you gaze at your fridge. This is where you kept your food, used to, anyway.')
            event.time_change(15)
            return self.fridge()
        elif action == '4':
            print('You stare at your fridge intensively. You are lost in your thoughts.')
            event.time_change(30)
            return self.fridge()
        else:
            event.invalid_input()
            return self.fridge()

    def freezer(self):
        if not self.check_freezer:
            print("You opened the freezer door. There are... some dead, frozen mice in your freezer. They are Monty's food.")
            self.check_freezer = True
        elif self.ate_mice:
            print("Your freezer is now empty.")
        else:
            print("There are some frozen mice in your freezer.")
        if self.ate_mice:
                action = input("""
    pick an action:
    [1]check freezer               [3]"..."
    [2]walk away                   [4]"......"
        """)
        else:
            action = input("""
    pick an action:
    [1]eat the mice                [3]"..."
    [2]walk away                   [4]"......"
        """)
        if action == '1':
            if not self.ate_mice:
                eat_mice = input("An intrusive thought flashes in your mind. Do you actually want to do it?(Y/N)").upper()
                if eat_mice == "Y":
                    print("You cooked the mice and ate them. It was a very unpleasant feeling.")
                    event.sanity_check(player.sanity, -50) 
                    self.ate_mice = True
                elif eat_mice == "N":
                    print("That was some ridiculous thoughts. You wouldn't have done it even if you're too hungry, right?")
            else:
                print("There's nothing left in your freezer.")
            return self.fridge()
        elif action == '2':
            return self.check_kitchen()
        elif action == '3':
            if not self.ate_mice:
                print('you gaze at the dead mice. The freezing air makes you feel a bit chilly. Maybe you should close the freezer door before your electricity bills go up.')
            else:
                print("You gaze at the empty freezer. Nothing but the hollow cold air blows on your face.")
            event.time_change(15)
            return self.freezer()
        elif action == '4':
            if not self.ate_mice:
                print('You stare at the cold, immobile corpses of some mice. The freezing air is blasting on your face. You are definitely not a stranger to these dead critters because of Monty. But why do they make you feel so uncomfortable?')
                sanity_check(player.sanity, -5)
            else:
                print("You stare at the empty freezer, reflecting on what you've done. With your pet snake's food, or your life.")
            event.time_change(30)
            return self.freezer()
        else:
            event.invalid_input()
            return self.freezer()

    def leave_apartment(self):
        if player.morning_routine:
            print("You left your apartment. It's time for grocery shopping.")
            return street.walking()
        else:
            print("You are not in a presentable state at all. You haven't even brushed your teeth. Maybe you should go to the bathroom and get ready for your day. ")
            leave = input("Are you sure you want to go outside in your current state? (Y/N) ").upper()
            if leave == "Y":
                print("You left your apartment in your pajamas and slippers. You probably smell a bit, too.")
                event.sanity_check(player.sanity, -10)
            else:
                return self.check_kitchen()

class Street(Location):
    def __init__(self):
        pass

    def walking(self):
        print("You are walking in the street.")

    def cult(self):
        pass

class GroceryStore(Location):
    pass

class Endings:
    pass




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
location = Apartment()
event = GlobalVariables()
street = Street()

name_confirm = input('Your character name is {0}, right? (Y/N) '.format(player.name)).upper()
while name_confirm == 'N':
    player.name = input("Name your character:\n")
    name_confirm = input('Your character name is {0}, right? (Y/N) '.format(player.name)).upper()
clear()
print("""
You woke up in your room.
It's currently early morning on a Saturday. Your stomach rumbles. It's time for breakfast.... Well, only if you didn't run out of food. You probably should stay on top of your grocery shopping.
So it's time to go get some food, and probably grocery as well.
It's time to step on a journey. A joureny to the grocery store.
""")
location.check_bedroom()

x = input('current testing ends.press enter to exit.')