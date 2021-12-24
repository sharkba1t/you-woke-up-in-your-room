import os
import sys
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=30, cols=100))

#For terminal
clear = lambda: os.system('cls')
width, height = os.get_terminal_size()

#Global Variables

class GlobalVariables:
    def __init__(self):
        self.location = "apartment"
        self.time = 800
        # format : 800 8 am 1230 12:30 pm
        self.start_time = 800
        #ending related
        self.is_ending = False
        self.died_of_hunger = False
        self.left_home = False
        self.bought_grocery = False
        self.ate_mice = False
        self.cult_scared = False
        self.join_cult = False
        self.cult_leader = False

    def time_change(self, number):
        total_change = int(str(self.time)[-2:]) + number
        hour = total_change // 60
        #I don't understand my own codes but I made base 60 work
        if (total_change >= 60):
            self.time += hour * 40 + number
        else:
            self.time += number
        print("current time: {0}:{1}".format(str(self.time)[:-2],str(self.time)[-2:]))
        self.hunger_change()
        #make these only appear once
        if 800 <= self.time < 1200:
            print("It's currently morning.")
        elif 1200 <= self.time < 1300:
            print("It's currently noon.")
        elif 1300 <= self.time < 1700:
            print("It's currently afternoon.")
        elif 1700 <= self.time < 1900:
            print("It's currently evening. The grocery store will close at 20:00.")
        if self.time >= 2200:
            self.is_ending = True
            return self.is_ending

    def hunger_level(self, hunger):
        player.hunger_level += hunger
        if hunger < 0:
            print("Your stomach rumbles a bit.")
        elif hunger > 0:
            print("You feel less hungry now.")
        #remove the line below after finish debugging
        #print("Hunger level:", player.hunger_level, "self.start_time value:", self.start_time)
        if player.hunger_level <= 0:
            self.is_ending = True
            self.died_of_hunger = True
            return self.check_ending()
        return player.hunger_level

    def hunger_change(self):
        start_time = self.start_time;
        if self.time - start_time >= 100:
            hour = (self.time - start_time) // 100
            self.hunger_level(-5 * hour)
            self.start_time += 100 * hour
        return start_time

    def sanity_check(self, number):
        player.sanity += number
        #remove the line below after finish debugging
        #print("Current Sanity:", player.sanity)
        if player.sanity < 80:
            print('you feel a bit uneasy')
        if player.sanity < 50:
            print('You begin to question if everything until this point is normal.')
        if player.sanity <= 0:
            player.filter = True
        
    def check_ending(self):
        if self.is_ending:
            clear()
            if self.died_of_hunger:
                return end.hunger()
            elif self.left_home == False:
                return end.hermit()
            elif self.join_cult:
                 return end.joined_cult()
            elif self.cult_leader:
                return end.become_cult_leader()
            elif self.bought_grocery:
                return end.normal_ending()
            else:
                return end.low_sanity()


    def invalid_input(self):
        print('please enter a valid response')

class Player:
    def __init__(self):
        self.name = ''
        self.hunger_level = 50
        self.sanity = 100
        self.carrying_monty = False
        self.morning_routine = False
        self.filter = False

    def change_name(self):
        self.name = input("Name your character:\n")
        name_confirm = input('Your character name is {0}, right? (Y/N) '.format(self.name)).upper()
        while name_confirm == 'N':
            self.name = input("Name your character:\n")
            name_confirm = input('Your character name is {0}, right? (Y/N) '.format(self.name)).upper()
        clear()

#All Dialogues
apartment_location_change = {
"room to kitchen": "you moved to the kitchen/living room",
"kitchen to room": "You went back to your room",
"bed": "You walked away form your bed.",
"tank": {
    "carrying Monty": "It\'s probably a bad idea to carry Monty with you right now.",
    "other": "You left Monty alone for now."
        },
"bathroom to kitchen": "you returned to the kitchen.",
"leave apartment": {
    "clean": "You left your apartment. It\'s time for grocery shopping.",
    "mess": "You left your apartment in your pajamas and slippers. You probably smell a bit, too."},
}

apartment_flavor_text = {
    "room": {"first time":  "You looked around your room. There\'s your bed, your pet snake Monty\'s tank, and your desk.",
    "other": "You are back at the center of your room."
    },
    "desk": "Your computer is on. It\'s on almost 24/7. Other than that, nothing else caught your attention here.",
    "bed": {
        "messy": "Your bed is messy. You should probably make your bed.",
        "tidy": "Your bed is now tidy."
        },
    "kitchen": {
        "first time" : "You are now in your kitchen/living room. The bathroom is to your right- that\'s also where you do half of your morning routine. The apartment door is in the front.",
        "other": "You are now in your kitchen/living room."
    },
    "tank": {
        "Monty in": "You looked at the tank. Your pet snake, Monty, a ball python, is napping in its hide.",
        "Monty out": "Monty is now resting on your arm."
    },
    "bathroom": "You are in the bathroom.",
    "fridge" : {
        "first time": "You opened the fridge door. There are a few soda cans left here, but other than that, there is nothing to eat here. Maybe there\'s still frozen food left in your freezer?",
        "other": "You stand in front of your fridge, a fridge without any human food.",
        "ate mice": "Your fridge is now out of food, including snake food."
    },
    "freezer": {
        "first time" : "You opened the freezer door. There are... some dead, frozen mice in your freezer. They are Monty\'s food.",
        "other": "here are some frozen mice in your freezer.",
        "empty": "Your freezer is now empty."
        }
}

class Apartment(GlobalVariables):
    def __init__(self):
        self.first_time_bedroom = True
        self.first_time_kitchen = True
        self.first_time_check_fridge = True
        self.bed_is_messy = True
        self.check_freezer = False

#Main actions - Bedroom
    def check_bedroom(self):
        while event.is_ending == False:
            self.location = "apartment"
            if self.first_time_bedroom:
                print(apartment_flavor_text["room"]["first time"])
                self.first_time_bedroom = False
            else:
                print(apartment_flavor_text["room"]["other"])
            action = input("""
    pick an action:
    [1]check desk       [4]go to kitchen/living room
    [2]check bed        [5]"..."
    [3]check tank       [6]"......"
        """)
            action = int(action)
            clear()
            if action == 1:
                return self.desk()
            elif action == 2:
                return self.bed()
            elif action == 3:
                return self.tank()
            elif action == 4:
                print(apartment_location_change['room to kitchen'])
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
        event.check_ending()

#Apartment specific areas

    def desk(self):
        event.check_ending()
        print(apartment_flavor_text['desk'])
        return self.check_bedroom()

    def bed(self):
        while event.is_ending == False:
            if self.bed_is_messy:
                print(apartment_flavor_text["bed"]["messy"])
            else:
                print(apartment_flavor_text["bed"]["tidy"])
            action = input("""
        pick an action:
        [1]sleep                  [4]"..."
        [2]make bed               [5]"......"
        [3]walk away
            """)
            clear()
            if action == '1':
                print("Screw responsibilities. it's time for a nap.")
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
        event.check_ending()

    def tank(self):
        while event.is_ending == False:
            if not player.carrying_monty:
                print(apartment_flavor_text["tank"]["Monty in"])
                action = input("""
        pick an action:
        [1]take Monty out of the tank        [3]"..."
        [2]walk away                         [4]"......"
            """)
            else:
                print(apartment_flavor_text["tank"]["Monty out"])
                print("Monty: pssssssst.")
                action = input("""
        pick an action:
        [1]put Monty back in the tank        [3]"..."
        [2]walk away                         [4]"......"
            """)
            clear()
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
        event.check_ending()

#Main actions - Kitchen
    def check_kitchen(self):
        while event.is_ending == False:
            self.location = "apartment"
            if self.first_time_kitchen:
                print(apartment_flavor_text["kitchen"]["first time"])
                self.first_time_kitchen = False
            else:
                print(apartment_flavor_text["kitchen"]["other"])
            action = input("""
        pick an action:
        [1]check the fridge                   [4]leave the apartment
        [2]go to the bathroom                 [5]"..."
        [3]go to the bedroom                  [6]"......"
            """)
            clear()
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
        while event.is_ending == False:
            self.location = "apartment"
            print(apartment_flavor_text["bathroom"])
            action = input("""
        pick an action:
        [1]Get ready for the day            [3]"..."
        [2]Go to kitchen/living room        [4]"......"
            """)
            action = int(action)
            clear()
            if action == 1:
                if not player.morning_routine:
                    print("......")
                    print("You finished your morning routine. You are ready to leave your apartment now.")
                    event.sanity_check(10)
                    event.time_change(30)
                    player.morning_routine = True
                else: 
                    print("You've already done that. It is now time for grocery shopping.")
                return self.bathroom()
            elif action == 2:
                print(apartment_location_change["bathroom to kitchen"]) 
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
        event.check_ending()

# Sub Spaces for Kitchen Area
    def fridge(self):
        while event.is_ending == False:
            if self.first_time_check_fridge:
                print(apartment_flavor_text["fridge"]["first time"])
                self.first_time_check_fridge = False
            elif event.ate_mice:
                print(apartment_flavor_text["fridge"]["ate mice"])
            else:
                print(apartment_flavor_text["fridge"]["other"])
            action = input("""
    pick an action:
    [1]check freezer               [3]"..."
    [2]walk away                   [4]"......"
            """)
            clear()
            if action == '1':
                return self.freezer()
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
        event.check_ending()

    def freezer(self):
        while event.is_ending == False:
            if not self.check_freezer:
                print(apartment_flavor_text["freezer"]["first time"])
                self.check_freezer = True
            elif event.ate_mice:
                print(apartment_flavor_text["freezer"]["empty"])
            else:
                print(apartment_flavor_text["freezer"]["other"])
            if event.ate_mice:
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
            clear()
            if action == '1':
                if not event.ate_mice:
                    eat_mice = input("An intrusive thought flashes in your mind. You thought of eating the dead mice. Do you actually want to do it?(Y/N) ").upper()
                    if eat_mice == "Y":
                        
                        print("You cooked the mice and ate them. It was a very unpleasant feeling.")
                        event.sanity_check(-50) 
                        event.hunger_level(50)
                        event.ate_mice = True
                    elif eat_mice == "N":
                        print("That was some ridiculous thoughts. You wouldn't have done it even if you're too hungry, right?")
                else:
                    print("There's nothing left in your freezer.")
                return self.freezer()
            elif action == '2':
                return self.check_kitchen()
            elif action == '3':
                if not event.ate_mice:
                    print('you gaze at the dead mice. The freezing air makes you feel a bit chilly. Maybe you should close the freezer door before your electricity bills go up.')
                else:
                    print("You gaze at the empty freezer. Nothing but the hollow cold air blows on your face.")
                event.time_change(15)
                return self.freezer()
            elif action == '4':
                if not event.ate_mice:
                    print('You stare at the cold, immobile corpses of some mice. The freezing air is blasting on your face. You are definitely not a stranger to these dead critters because of Monty. But why do they make you feel so uncomfortable?')
                    event.sanity_check(-5)
                else:
                    print("You stare at the empty freezer, reflecting on what you've done. With your pet snake's food, or your life.")
                event.time_change(30)
                return self.freezer()
            else:
                event.invalid_input()
                return self.freezer()
        event.check_ending()

    def leave_apartment(self):
        if event.left_home == False:
            if player.morning_routine:
                print(apartment_location_change["leave apartment"]["clean"])
                event.left_home = True
                return street.walking()
            else:
                print("You are not in a presentable state at all. You haven't even brushed your teeth. Maybe you should go to the bathroom and get ready for your day. ")
                leave = input("Are you sure you want to go outside in your current state? (Y/N) ").upper()
                if leave == "Y":
                    print(apartment_location_change["leave apartment"]["mess"])
                    event.sanity_check(-10)
                    event.left_home = True
                    return street.walking()
                else:
                    return self.check_kitchen()
        else:
            print("You left your apartment.")
            return street.walking()


#Street and cult
class Street(GlobalVariables):
    def __init__(self):
        self.location = "street"
        self.way_to_grocery = 0
        # 0: home, 5: cult 10: grocery store
        self.first_time_cult = False
        self.read_sign = False
        self.cult_dialogue = [
            "This is your opportunity to learn about the universe we are in. The facts, how it operates- everything.",
            "What you've learned about the universe previously is mostly misconceptions due to people's ignorants.",
            "The world will end soon. In fact, it's ending right now.",
            "People refuse to acknowledge the facts and continue to escalate the process.",
            "Entropy is a measurement of the degree of disorder—your actions, whether the society deems moral, immoral, right, wrong, rewardable or not, will escalate the entropy of the universe.",
            "The entropy of the universe is increasing. At our organization, we monitor all activities of the entropy. They have been abnormal recently.",
            "We, the children of the Void, are all like-minded. The void is inclusive and non-judgmental, and so are we.",
            "We gather together to prepare for the end… and we will face the end with inner peace. We do not mean to cause panic or fear.",
            "Do we believe in the afterlife? Yes and no. The world is born from the void. Once we perish, we will return to the void. Our minds and souls, to be exact.",
            "We are selective of our members. While we want to spread the knowledge, only the selected few can join us and oversee the progression of the world's end."
            ]
        self.cult_dialogue_counter = 0
        self.cult_intimidation = 0
        self.cult_interrupted = False
        self.cult_uneasy = 0
        self.cult_finish_talking = False

    def walking(self):
        while event.is_ending == False:
            print("You are walking in the street.")
            action = input("""
    pick an action: 
        [1]keep walking        [3]"..."
        [2]go home             [4]"......"
        """)
            action = int(action)
            clear()
            if action == 1:
                print("You walk down the street.")
                event.time_change(5)
                self.way_to_grocery += 5
                if event.time < 1700:
                    return self.midway()
                else:
                    return self.midway_evening()
            elif action == 2:
                if event.bought_grocery == False:
                    print("The outside world is too much for you, afterall.")
                    return home.check_kitchen() 
                else: 
                    event.is_ending = True
                    clear()
                    return end.normal_ending() 
                    #change this directly to the ending later
            elif action == 3:
                print("You stand idlly on the street")
                event.time_change(15)
                return self.walking()
            elif action == 4:
                print("You stand idlly, staring at the pedestrians.")
                event.time_change(30)
                return self.walking()
            else:
                event.invalid_input()
                return self.walking()

    def midway(self):
        while event.is_ending == False:
            self.location = "street"
            if self.cult_intimidation >= 10 or self.cult_uneasy >= 4 :
                event.cult_scared = True
            if not self.first_time_cult and self.cult_intimidation < 10:
                print('You see a couple of people standing on the sidewalk. They all wear robes for some reason. There are some signs next to them.')
            elif  self.cult_intimidation >= 10:
                print('This group of people is intimidated by your silent stares, but no one wants to be the one to tell you to leave.')
            elif self.cult_interrupted == True:
                print('This group of people is still here. They gave you a weird look.')
            elif store.went_to_store:
                print('On your way home, the group of people is still here.')
            else:
                print("A mysterious group of people is standing here with signs next to them.")
            action = input("""
    pick an action: 
    [1]read signs             [4]"..."
    [2]keep walking           [5]"......"
    [3]go home
        """)
            action = int(action)
            clear()
            if action == 1:
                print('"The world will end soon! The entropy of the universe is approaching its limits, and your actions only escalate the process." \n "Join us. We will face the end together, and we will meet again in the void."')
                if self.read_sign == False:
                    if self.cult_intimidation < 10:
                        print("One of the people notices you are reading the sign.")
                    else:
                        print("One of them wants to start a conversation, but they are too scared to talk to you.")
                self.read_sign = True
                event.time_change(5)
                return self.midway()
            elif action == 2:
                print("You brush off those weirdos, and keep walking towards the grocery store.")
                self.way_to_grocery += 5
                return store.grocery_store()
            elif action == 3:
                print("You decided the outside world isn't worth your time today, so you turned around and go home.")
                event.time_change(5)
                return home.check_kitchen() 
                pass 
            elif action == 4:
                if self.read_sign == False:
                    print('You gaze at the group. It doesn\'t seem that they want to enegage in conversations with you yet. Maybe they\'ll talk to you once you read the signs?')
                    event.time_change(5)
                    return self.midway()
                elif self.cult_intimidation >= 10 or self.cult_uneasy >= 4:
                    print('The group of people seems to be intimidated by your silence. No one wants to talk to you.')
                    return self.midway()
                elif self.cult_interrupted == True:
                    print('It doesn\'t seem like they want to talk to you anymore.')
                else:
                    print("???: It seems that you are interested in our orginzation.")
                    print("One of the members starts a conversation with you.")
                    print("The member begins to tell you more about the organization.")
                    return self.cult()
                return self.midway()
            elif action == 5:
                if self.read_sign == False:
                    if (self.cult_intimidation < 10) or (self.cult_uneasy < 4):
                        print('You stare at the group of people. They are trying their best to stay silent. One of them is visibly afraid the attention you are giving them.')
                        self.cult_intimidation += 2
                        event.time_change(10)
                        return self.midway()
                elif self.cult_intimidation >= 10 or (self.cult_uneasy >= 4):
                    print('???: Can you... leave us alone, please?')
                    print("One of the members finally speaks. His voice is shaking.")
                    return self.midway()
                elif self.cult_interrupted == True:
                    print('It doesn\'t seem like they want to talk to you anymore.')
                    return self.midway()
                else:
                    print("???: Are you... Interested in hearing about our cause?")
                    print("One of the members hesitates before he talks to you.")
                    print("The member begins to tell you more about the organization.")
                    return self.cult()
            else:
                event.invalid_input()
                return self.midway()
        event.check_ending()

    def midway_evening(self):
        while event.is_ending == False:
            self.location = "street"
            if self.first_time_cult == False:
                print("You are halfway to the grocery store. Only some pedestrians and a few cars are on the street.")
            else:
                print("The group of people that was here are now gone. So are the signs.")
            action = input("""
    pick an action: 
    [1]keep walking            [4]"..."
    [2]go home                 [5]"......"
        """)
            action = int(action)
            clear()
            if action == 1:
                print('You keep walking down the street.')
                event.time_change(5)
                return store.grocery_store()
            elif action == 2:
                if event.bought_grocery == False:
                    print("The outside world is too much for you, afterall.")
                    return home.check_kitchen() 
                else: 
                    event.is_ending = True
                    return event.check_ending()
                return 
            elif action == 3:
                print('You stand in the middle of the street, looking at people walking by.')
                event.time_change(15)
                return self.midway_evening()
            elif action == 4:
                print("You stare at the pedestrians. Some of them is put off by your stare.")
                event.time_change(30)
                return self.midway_evening()
            else:
                event.invalid_input()
                return self.midway_evening()
        event.check_ending()

    def cult(self):
        while self.cult_dialogue_counter < 9 : 
            if self.cult_uneasy >= 4:
                print('"……" the person took a step back as they stopped talking. "If you don\'t believe us or are in a hurry, you could\'ve let me know. I would have let you go…"')
                return self.midway()
                break
            else:
                print("???:", self.cult_dialogue[self.cult_dialogue_counter])
                action = input("""
        Pick an action:
        [1]Go home                      [3]"..."
        [2]Go to the Grocery Store      [4]"......"
                """)
                clear()
                if action == "1":
                    print("You walk away from the enthuiastic member, they seem to be shocked by the fact that you just walked away.")
                    print("You begin to head home.")
                    self.cult_interrupted = True
                    return home.check_kitchen()
                    break
                elif action == "2":
                    print("You walk away from the enthuiastic member, they seem to be shocked by the fact that you just walked away.")
                    print("You head to the grocery store.")
                    self.cult_interrupted = True
                    return store.grocery_store()
                    break
                elif action == "3":
                    print("You continue to listen to them talking.")
                    self.cult_dialogue_counter += 1
                    event.time_change(10)                    
                elif action == "4":
                    print("The person hesitates a bit, and then keep talking.")
                    self.cult_uneasy += 1
                    self.cult_dialogue_counter += 1
                    event.time_change(10)    
                else:
                    event.invalid_input()
                    return self.cult()
        if player.sanity <= 40:
            if self.cult_finish_talking == False:
                print('"...!"')
                print('The cult member notices and stops themselves from talking.')
                print('"There is somthing in your eyes... I can see the void in your eyes!"')
                print("\"In the propercy, it says a person with hollow eyes like your will lead us to the right way.\"")
                print('"Please, you must join us and become our leader."')
                self.cult_finish_talking = True
            else:
                print('???:"You are back! Did you change your mind?"')
            become_cult_leader = input("Will you become their leader?(Y/N)").upper()
            if become_cult_leader == "Y":
                print("You nod. The group seems happy.")
                event.is_ending = True
                event.cult_leader = True
                return self.midway()
            elif become_cult_leader == "N":
                print("You shake your head. The group seems disappointed, but they respect your decision.")
                print("???: If you ever change your mind, please come back and guide us...")
            else:
                event.invalid_input()
                return self.cult()
            return self.midway()
        else:
            join_cult = input("\"Now that you have heard about our orginization, would you like to come with us to our next meeting?\" (Y/N)").upper()
            if join_cult == 'Y':
                print("You nodded. They hand you a card. There's an address on it. ")
                event.is_ending = True
                event.join_cult = True
                return self.midway()
            elif join_cult == 'N':
                print("You shake your head. \"Very well, but we will be here if you change your mind.\"")
                return self.midway()
            else:
                event.invalid_input()
                return self.cult()


#Grocery Store

class GroceryStore(GlobalVariables):
    def __init__(self):
        self.weight = 0
        self.went_to_store = False
        self.have_grocery = False
    
    def grocery_store(self):
        while event.is_ending == False:
            self.location = "store"
            if event.time < 2000:
                print("You arrived at the grocery store.")
                action = input("""
        Pick an action:
        [1]get essential groceries     [4]leave store
        [2]get extra groceries         [5]"..."
        [3]Get snacks                  [6]"......"
                """)
                action = int(action)
                clear()
                if action == 1:
                    print("You pick up some essential groceries. It will last you for about a week.") 
                    self.weight += 10;
                    self.have_grocery = True
                elif action == 2:
                    print("You pick up enough grocery to last you 2 weeks.")
                    self.weight += 20; 
                    self.have_grocery = True
                elif action == 3:
                    print("You pick up some snacks. Cooking meals is too much work.")
                    self.weight += 10;
                    self.have_grocery = True
                elif action == 4:
                    if self.have_grocery:
                        print("You paid for your groceries, and left the store")
                        event.time_change(30)
                        event.bought_grocery = True
                    else:
                        print("You left the store without buying anything.")
                        event.time_change(5)
                    self.went_to_store = True
                    return street.walking()
                elif action == 5:
                    print("You stand at the grocery store, gazing at everyone around you.")
                    event.time_change(15)
                elif action == 6:
                    print("You stare at everyone walking pass you.")
                    event.time_change(30)
                else:
                    event.invalid_input()
                    return self.grocery_store()
            else:
                print("The grocery store is closed. Hours: 8:00 AM ~ 8:00 PM")
                print("You are now standing in front of the closed grocery store.")
                action = input("""
        Pick an action:
        [1]Go home              [2]"..."
                                [3]"......"
                """)
                action = int(action)
                clear()
                if action == 1:
                    print("You decided to go home.")
                    event.is_ending = True
                    return self.grocery_store() 
                elif action == 2:
                    print("You gaze at the closed doors. The lights are off in the store.") 
                    event.time_change(15)
                    return self.grocery_store()
                elif action == 3:
                    print("You gaze at the closed doors. The lights are off in the store.")
                    event.time_change(30)
                    return self.grocery_store()
                else:
                    event.invalid_input()
                    return self.grocery_store()
        event.check_ending()

class Endings(GlobalVariables):
    def test_ending(self):
        print("Everything works until this point.")

    def normal_ending(self):
        clear()
        #you get here if you act like a normal human: get ready for leaving, not join the cult, get grocery, and get home
        print("You arrived home with food. You then make and eat your meal. Another ordinary day has passed.")
        if event.ate_mice:
            print("...Except the fact that you ate some frozen mice to stop feeling hungry.You need to get more for Monty at some point.")
        if event.cult_scared:
            print("You continue your life as normal. There isn't any changes to the world. Except, you haven't seen that group of weird people in this area again.")

    def low_sanity(self):
        clear()
        if event.location == "street":
            print("You wander aimlessly on the street. You survived today, but what about tomorrow?")
        if event.location == "apartment":
            print("You are back in your apartment. You didn't get any groceries, but somehow you survived the day.")
            print("Eventually you will have to leave for food again, whether it's for Monty or yourself.")
        print("But that doesn't matter anymore. You feel a strong attraction towards the void. You don't know what the void is, nor you can describe it, but you know it's there. It'll always be there for you.")

    def hunger(self):
        clear()
        if event.location == "apartment":
            print("Your surrounding fades away from you.")
            print("A few days later, you are found dead in your own apartment.")
        elif event.location == "street":
            print("You collapsed on the street.")
            print("When you wake up again, you are in a hospital. Apparently some pedestrian saw you fall on the street, and you were rushed to the hospital.")

    def hermit(self):
        clear()
        print("It's currently midnight. You are still in your apartment. You never left during the day, and you somehow found a way to survive -- at the cost of your pet snake's food.")
        print("But the outside world is too dangerous. You don't want to leave.")

    def joined_cult(self):
        clear()
        print("You follow the group to a building. Inside the building, everyone sits in a circle and talk to each other.")
        print("After some introduction, they deem you a member of the orginization. As a welcoming party, they make you a nice meal.")
        print("You don't have to worry about groceries for now.")

    def become_cult_leader(self):
        clear()
        print('"We would like to introduce you to our new and only leader, {0}. Under their leadership, we will lead the world to salvation."'.format(player.name))
        print("You stand in front of a group of people in robes. They are waiting for you to say something.")
        print('"......"')
        print('Your look at everyone with your hollow eyes.')
        print('A month has passed since you agreed to become their leader.')
        print('Surprisingly, there isn\'t much for you to do here. Everything is prepared for you. Monty\'s new and fancy tank sits next to you. It seems that the organization is worshipping Monty as well, for some reason.')
        print('At least you don\'t have to worry about getting groceries now.')




#Gameplay starts here
clear()

print("""

    ------------------------------------------------------------
        You Woke Up In Your Room On A Saturday Morning
    ------------------------------------------------------------


""")

# initialization
event = GlobalVariables()
player = Player()
home = Apartment()
street = Street()
store = GroceryStore()
end = Endings()
player = Player()

player.change_name()
print("""
You woke up in your room.
It's currently early morning on a Saturday. Your stomach rumbles. It's time for breakfast.... Well, only if you didn't run out of food. You probably should stay on top of your grocery shopping.
So it's time to get some food, and probably groceries as well.
It's time to step on a journey—a journey to the grocery store.
""")

home.check_bedroom()

x = input("""
This is the end of the game. Thanks for playing!
(press Enter to exit)
""")