from game.console import Console
from game.seeker import Seeker
from game.hider import Hider

class Director:
    def __init__(self):
        self.console = Console()
        self.seeker = Seeker()
        self.keep_playing = True
        self.hider = Hider()
        
    def start_game(self):
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        message = self.seeker.get_message()
        self.console.write(message)
        location = self.console.read_number("Enter a location [1-1000]: ")
        self.seeker.move(location)
        
    def do_updates(self):
        self.hider.watch(self.seeker.location)
        
    def do_outputs(self):
        hint = self.hider.get_hint()
        self.console.write(hint)
        self.keep_playing = (self.hider.distance[-1] != 0)