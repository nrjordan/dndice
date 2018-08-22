import random


class Dice:

    def __init__(self, sides):
        self.dice_num = 1
        self.die_sides = sides

    def roll(self):

        results = []

        for i in range(self.dice_num):
            results.append(random.randint(1, self.die_sides))

        return results
