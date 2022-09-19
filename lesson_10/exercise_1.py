from random import randint
class Dice:    
    def roll(min, max):
        return randint(min, max)

class D20(Dice):
    def roll():
        return randint(1, 20)

d = Dice
print(d.roll(1,10))

d20 = D20
print(d20.roll())