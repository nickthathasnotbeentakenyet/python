import random

class Thrower:
    def __init__(self) -> None:
        self.dice = []
        self.num_throws = 0

    def can_throw(self):
        if self.dice.count(5) > 0 or self.dice.count(1) > 0 or self. num_throws == 0: return True
        else: return False
        
    def get_points(self):
        return self.dice.count(5) * 50 + self.dice.count(1) * 100
    
    def throw_dice(self):
        self.dice.clear()
        for _ in range(5):
            dice = random.randint(1,6)
            self.dice.append(dice)
        self.num_throws += 1