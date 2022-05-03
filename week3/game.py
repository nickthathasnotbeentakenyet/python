import sys
import time
# declare function for gameover
def gameover():
    print("\n= GAME OVER =\n¯\_(ツ)_/¯\n")
# heading
print()
print("="*50)
print("="*13 + " WELCOME TO GAME WORLD " + "="*14)
print("="*50 + "\n")

# the game
print("You wake up in a complete darkness. You look around and find a computer and a keyboard connected to it.")
time.sleep(5)
print("Suddenly, you notice the letters start appearing on the screen ")
time.sleep(2)
caption = '"Please enter your name: "'
for i in caption:
    print(i, end='')
    sys.stdout.flush()
    time.sleep(0.1)   
username = input("\n> ")
print(f"\nHello, {username}. I'm glad you remember your name, because your memory has been reset to almost 0. I am your only friend here.")
print("You have been making bad decisions lately. So I am going to teach you a lesson about consequences")
print("Every move, every decision changes your future. Be wise in your decisions. May the Game begin!")
time.sleep(10)
print("The cursor on the screen is blinking, ready for you to accept commands. You look around and can't see anything")
time.sleep(3)
print("You realize that computer was left to help you. Enter one of the commands: [LIGHTS or POWEROFF]")
time.sleep(3)
answer_first = input("\n> ")
if answer_first.lower() == "poweroff":
    print("You just turned OFF the computer. You are surrounded by complete darkness and can't even find the button to turn it back ON")
    time.sleep(2)
    print("You're trying to find something in the dark. After a long search and walking in the dark, you manage to find a flashlight.")
    time.sleep(2)
    print("What do you want to do with it? [TURN ON or PUT DOWN]")
    time.sleep(2)
    answer_flashlight = input("\n>")
    if answer_flashlight.lower() == "put down":
        print("\"Yes\", you thought. Someone clearly wants me to use the flashlight. Someone wants me to play by their rules.")
        print("But time passes, and sitting alone in the dark becomes too creepy. So you decide to pick up the flashlight and turn it ON")
    else:
        print("Wise decision. You press the power button and the flashlight sends a beam of light forward")
    print("Now that there is at least some light, you dare to look around.")
    print("You are in a windowless room with a locked door and a computer turned off.")
    print("You go around the back of the computer and find the power button.")
    print("What do you want to do with it? [PRESS or EXPLORE]")
    answer_button = input("\n> ")  
    if answer_button.lower() == "press":
        print("Computer starts booting...")
        time.sleep(2)
        print("The flashlight starts blinking. Apparently, the batteries inside are very discharged.")
        print("You don't want to be in complete darkness at all. Fortunately, the computer has already booted up and is ready to accept commands.")
        print(f"\"Thank you, {username}, for turning me back ON. I hope you now realize that I'm your best friend here.")
        print("I will help you out, if you let me. But it is always your decision what to do.")
        print("What do you want me to do next for you?\" Enter one of the commands: [LIGHTS or POWEROFF]")
        answer_rebooted = input("\n> ")
        if answer_rebooted.lower() == "poweroff":
            print("You screwed up. Life teaches you nothing. You left yourself no choice. You will stay here in the dark alone forever.")
            print("\n= GAME OVER =\n")
            exit(0)
        elif answer_rebooted.lower() == "lights":
            print("The room is illuminated by a bright light. How timely!")
            print("Your flashlight has just stopped working, but now you don't need it. You can finally look around without help.")
            print("You go to the door and try to open it. Unfortunately it is locked securely.")
            time.sleep(3)
            print("\nNow what?\n - You speak to yourself")
            print("Walking from corner to corner, you decide to return to your only \"friend\"")
        else:
            print("You scratch you head. Think twice. And finaly decide to put the lights ON")    
            print("Walking from corner to corner, you decide to return to your only \"friend\"")
    elif answer_button.lower() == "explore":
        print("You go around the room several times in a row and find nothing in it.")
        print("No secret passage, no clue about how you got here and how to get out.")
        print("Walking from corner to corner, you decide to return to your only \"friend\"")  
    print("You notice a new message left on the screen.")
    print(f"{username.capitalize()}, do you want me to let you out? [YES or NO]")
    answer_out = input("\n> ")
    if answer_out.lower() == "yes":
        print("The monitor screen begins to flicker like flashes of lightning and fireworks in the night sky.")
        print("The color representation suddenly covers the entire room. You lose consciousness.")
        time.sleep(3)
        print(f"{username}! {username}! Do you hear me?")
        print("You open your eyes and see your room, in your parents' house. Mom calls you and your siblings for breakfast.")
        print(f"You glance to the side. Near the window, on the table is your old computer, on which the caption flashes: \"Goodbye, {username}...\"\n\(◦'⌣'◦)/\n")
        exit(0)
    else:
        print("I knew you wouldn't let me stay alone here for ever, my friend. Only you and me.")
        print("You have found a frind. But it was a bad decision")
        time.sleep(3)
        gameover()
elif answer_first.lower() == "lights":
    print("The computer sends a signal to the lighting system and the room is lit up with light") 
    print("You look around you and all you see is a door.")
    print("What do want to do with the door? [OPEN or KNOCK]")
    answer_door = input("\n> ")
    if answer_door.lower() == "open":
        print("The door is locked.")
        print("you're trying to break it. \nRunning away from the wall, you jump with all your strength with your whole body onto the door in the hope of breaking it down.")
        print("Surprisingly, the door easily flies off its hinges and with it you fall into the void. Dark and endless.")
        time.sleep(8)
        gameover() 
    elif answer_door.lower() == "knock":
        print("You knock on the door three times. With every knock, the room you're in starts to shake.")
        time.sleep(2)
        print("It was as if someone had knocked on the room itself... The walls begin to crumble and you're buried by the remains of the walls.")
        time.sleep(7)
        gameover()   
    else:
        print(f"\"{answer_door}\" is unexpected command, but know what? I'm gonna play it.")
        print("No matter what you do, the door doesn't open. This door doesn't even have a handle.")
        print("But still there's a keyhole. What would you do? [LOOK or LISTEN]")
        time.sleep(2)
        answer_keyhole = input("\n> ") 
        if answer_keyhole.lower() == "listen":
            print("Leaning your ear, you try to hear at least something. Even a terrible sound now would be better than complete silence.")
            print("On the other side of the door, only a slightly rapid heartbeat can be heard. As if someone is there and feels a quiet horror.")
            print("Finally you dare to look through the hole in the door")
        else:
            print("Crouching slightly so that the keyhole was at eye level, you turned your gaze inward.")
        print("There was one eye on the other side of the door watching at you. No, it's nobody else but yourself. \nIt's like someone put you in the next room so you can free yourself.")  
        print("This horror instantly fills you with panic and you fall dead.")
        time.sleep(10)
        gameover()        
else:
    print(f"The computer reads you command, but it's programmed to only accept certain commands. So when you entered \"{answer_first}\", it crashed.")
    print("You are now left alone in darkness with no help. Nobody knows where you are.") 
    print("In your head you keep spinning the same thought over and over again")
    print("I shouldn't have made a mistake. I shouldn't have made a mistake. I shouldn't have made a mistake.")
    print("But it was too late...")
    time.sleep(3)
    gameover() 
