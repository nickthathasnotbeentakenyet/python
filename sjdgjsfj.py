#import randint , and we will use it to generate random integer 
from random import randint


# function to show the game board , it has a list as an argument 
def show(TAB):
    print(f"{TAB[0]}  |  {TAB[1]}  |  {TAB[2]}\n--------------\n{TAB[3]}  |  \
{TAB[4]}  |  {TAB[5]}\n--------------\n{TAB[6]}  |  {TAB[7]}  |  {TAB[8]}\n")


#when player X or Y takes his turn we will call this function to check if that player won
def checkwinner(TAB):
	#check if player X won , if player X won it will return 'X'
    if ((TAB[6]=='X' and TAB[7]=='X' and TAB[8]=='X') \
        or (TAB[3]=='X' and TAB[4]=='X' and TAB[5]=='X') \
        or (TAB[0]=='X' and TAB[1]=='X' and TAB[2]=='X')\
        or (TAB[6]=='X' and TAB[3]=='X' and TAB[0]=='X') \
        or (TAB[7]=='X' and TAB[4]=='X' and TAB[1]=='X') \
        or (TAB[8]=='X' and TAB[5]=='X' and TAB[2]=='X')  \
        or (TAB[6]=='X' and TAB[4]=='X' and TAB[2]=='X') \
        or (TAB[0]=='X' and TAB[4]=='X' and TAB[8]=='X')):
        return'X'
    # check if player Y won , if player Y won it will return 'Y'
    elif ((TAB[6]=='Y' and TAB[7]=='Y' and TAB[8]=='Y') \
        or (TAB[3]=='Y' and TAB[4]=='Y' and TAB[5]=='Y') \
        or (TAB[0]=='Y' and TAB[1]=='Y' and TAB[2]=='Y')   \
        or (TAB[6]=='Y' and TAB[3]=='Y' and TAB[0]=='Y') \
        or (TAB[7]=='Y' and TAB[4]=='Y' and TAB[1]=='Y') \
        or (TAB[8]=='Y' and TAB[5]=='Y' and TAB[2]=='Y')  \
        or (TAB[6]=='Y' and TAB[4]=='Y' and TAB[2]=='Y') \
        or (TAB[0]=='Y' and TAB[4]=='Y' and TAB[8]=='Y')):
        return 'Y'
    # returns none, which means no one won yet
    else:
        return None

#initial condition to get in the while loop , initialise init string with 'yes' 
#in order to avoid case sensitive problems we are going to use  .lower()  method to convert the string to lower case 
#if the player gave the value 'YES' or 'yeS'.. as an input, it will be converted to => 'yes'
init ='yes'
while init.lower()=='yes':
	# ask the player for an answer 
    init = input("Do You Want to play X/O :  [YES/NO] ")
    # if his answer was no we will print 'THE END' and get out of the game
    if (init.lower() == "no"):
        print("THE END")
    # else, we will start playing
    else:
    	#game_still = True   means that the game it's still, 
        # once one of those players won we will assigne the value False to that boolean
        game_still = True
        #a list contains the items of our game board 
        available_range = [7, 8, 9, 4, 5, 6, 1, 2, 3]
        #print the game board 
        show(available_range)
     	# the first player will be generated randomly 
        # generate random integer from the range [0,1] , if is it  1 means player X  will play first, 
        # if is it 0 means player Y  will play first
        playerx = randint(0,1)
        print("Generating Random player ... ")

        while (game_still):
        	# PLAYER X
        	# if playerx = 1   player X will play first
            if playerx == 1:
                print("=====================================\nPLAYER  X")
                # ask player X for input , player X going to choose a number from the available range list 
                xchose=int(input(f"choose number from range {available_range} : "))
                print("=====================================\n")
                # if player X chose an unvailable number ,we will give him another chance 
                if xchose not in available_range:
                    print(f"\n\n\n\nitem {xchose} is no longer available, choose again please!")
                # else , the number was in the available range
                else:

                    # we will use this for loop to search for the index of the number given by the player x, 
                    # when we will find the index , we will assigne the value 'X' to that item to indicate that the item 
                    # is no longer available in the range 
                    # the function enumerate() going to return th index and th values of each item in that list 
                    for i,j in enumerate(available_range):
                    		 # i : is the index of the items   , j = is the value of the item 
                             if (xchose==j):	# looking for the item 
                                  # assigning the 'X' to indicate that this item is no longer available in the range
                                  available_range[i] = 'X'		
                                  # show the game board 
                                  show(available_range)			
                                  # call the checkwinner function to check if the player X won or not 
                                  if (checkwinner(available_range)) == 'X':
                                      print('='*24+'\nCongratulations\n'+'='*24+'\nWINNER IS PLAYER X\n'+'='*24)
                                      # if player x won , we will end the game by assigning the value False into this boolean, 
                                      # which going to interrupt the while loop
                                      game_still = False

            		# assigne the value 0 to playerx  which means, it's the turn of the other player to play
                    playerx = 0


            # PLAYER Y
            # else, player Y play first
            else:
            	# the same algorithm as player X
                print("=====================================\nPLAYER  Y")
                ychose = int(input(f"choose number from range {available_range} : "))
                print("=====================================\n")
                if ychose not in available_range:
                    print(f"\n\n\n\nitem {ychose} is no longer available, choose again please!")
                else:
                    playerx = 1
                    for i, j in enumerate(available_range):
                        if (ychose == j):
                            available_range[i] = 'Y'
                            show(available_range)
                            if (checkwinner(available_range)) == 'Y':
                                print('='*24+'\nCongratulations\n'+'='*24+'\nWINNER IS PLAYER X\n'+'='*24)
                                game_still = False



