import random

class Seeker:
    def __init__(self):
        self.location = random.randint(1, 1000)
        self.distance = [0, 0] # start with two so get_message always works
    
    def get_message(self):
        message = "\nI'm going to find you!"
        if self.distance[-1] == 0:
            message = "\nI'm going to find you!"
        elif self.distance[-1] < self.distance[-2]:
            message = "\nShhh. I'm sneaking in now..."
        elif self.distance[-1] > self.distance[-2]:
            message = "\nI'm running around, but I'll find you..."
        return message

    def move(self, location):
        distance = abs(self.location - location)
        self.distance.append(distance)
        self.location = location