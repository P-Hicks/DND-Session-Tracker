#dice

import random

class Dice:
    def roll(die, adv = 0):
        dice = die.split("d")
        
        num_of_rolls = int(dice[0])
        if dice[1].find('+') != -1:
            storage_list = dice[1].split('+')
            die_type, added = int(storage_list[0]), int(storage_list[1])
        else:
            die_type, added = int(dice[1]), 0

        total = 0

        for i in range(num_of_rolls):
            if adv >= 0:
                long = 0
                for i in range(adv+1):
                    short = random.randint(1,die_type)
                    if short > long:
                        long = short
                total += long
            if adv < 0:
                long = 10000
                for i in range(-adv):
                    short = random.randint(1,die_type)
                    if short < long:
                        long = short
                total += long
        total += added

        return total


