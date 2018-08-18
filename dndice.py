import random


class Dice:

    def __init__(self):
        self.dice_num = 1
        self.die_sides = 20

    def roll(self):

        results = []

        for i in range(self.dice_num):
            results += random.randint(0, self.die_sides)
