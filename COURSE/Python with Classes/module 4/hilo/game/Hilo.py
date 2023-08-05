from game.Throw import Throw

class Hilo:
    pass

    def __init__(self) -> None:
        self.keep_playing = True
        self.score = 300
        self.thrower = Throw()
        self.guess = ""
        self.card1 = -1
        self.card2 = -1
        
        
    def start_game(self):
        while self.keep_playing:
            self.get_card1()
            self.get_input()
            self.get_card2()
            self.compare()
            self.playing()

    def get_card1(self):
        self.card1 = self.thrower.throw_card()
        print(f"\nThe card is: {self.card1}")

    def get_card2(self):
        self.card2 = self.thrower.throw_card()
        print(f"Next card was: {self.card2}")

    def get_input(self):
        self.guess = input("Higher or lower? [h/l] ")

    def compare(self):
        if (self.card1 < self.card2) and self.guess == "h": self.score += 100
        elif (self.card1 > self.card2) and self.guess == "l": self.score += 100
        else: self.score -= 75
        
    def playing(self):
        print(f"Your score is: {self.score}")
        choice = input("Keep playing? [y/n] ")
        if (choice not in ["y",""]) or self.score <=0 : self.keep_playing = False
