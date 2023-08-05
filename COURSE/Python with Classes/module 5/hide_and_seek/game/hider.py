import random

class Hider:

    def __init__(self) -> None:
        self.location = random.randint(1, 1000)
        self.distance = [0,0]

    def get_hint(self):
        message = ""
        if self.distance[-1] == 0:
            message = "\n(;.;) You found me!"
        elif self.distance[-1] > self.distance[-2]:
            message = "\n(^.^) Getting colder!"
        elif self.distance[-1] < self.distance[-2]:
            message = "\n(>.<) Getting warmer!"
        return message

    def watch(self, location):
        self.distance.append(abs(self.location - location))
