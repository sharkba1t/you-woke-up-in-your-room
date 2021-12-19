import random


class Player:
    def __init__(self, name):
        self.name = name
        self.hunger_level = 50
        self.money = 50

    def statGenerator(self):
        confirm = False
        while not confirm:
            pass

name = input("Name your character ")

player = Player(name)

yes_or_no = input('Your character name is {0}, right? (Y/N) '.format(player.name)).upper()
while yes_or_no == 'N':
    player.name = input("Name your character ")
    yes_or_no = input('Your character name is {0}, right? (Y/N)'.format(player.name)).upper()