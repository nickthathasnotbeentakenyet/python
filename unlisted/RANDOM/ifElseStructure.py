print("Hope this helps someone")
answer1 = input("Bla-bla-bla. What is your response? [ANSWER1 or ANSWER2] ")
if answer1.lower() == "answer1":
    print("this will only be executed if user said 'ANSWER1' ")
    # lets go dipper 1 level. This is level 2
    answer2 = input("Bla-bla-bla. What is your response? [LEVEL2_OPTION1 or LEVEL2_OPTION2] ")
    if answer2.lower() == "level2_option1":
        print("this will only be executed if user said 'LEVEL2_OPTION1")
    elif answer2.lower() == "level2_option2":
        print("this will only be executed if user said 'LEVEL2_OPTION2")
        # lets add level 3 here, because why not 
        answer3 = input("Bla-bla-bla. What is your response? [LEVEL3_OPTION1 or LEVEL3_OPTION2]")
        if answer3.lower() == "level3_option1":
            print("this will only be executed if user chose 'LEVEL3_OPTION1")
            # how about level 4? :D
            answer4 = input("Bla-bla-bla. What is your response? [LEVEL4_OPTION1 or LEVEL4_OPTION2 or LEVEL4_OPTION3]")
            if answer4.lower() == "level4_option1":
                print("this will only be executed if user chose 'LEVEL4_OPTION1")
            elif answer4.lower() == "level4_option2":
                print("this will only be executed if user chose 'LEVEL4_OPTION2")
            elif answer4.lower() == "level4_option3":
                print("this will only be executed if user chose 'LEVEL4_OPTION3")
            else:
                # in case user answered with smth completely different on level 4
                print("this will only be executed if user typed smth OTHER THAN the three options above")
        else:
            # do something for level 3 option 2 AND in case user said something else
            print("this will only be executed if user did NOT shoose LEVEL3_OPTION1")  
    else:
        # in case user answered with smth completely different on level 2
        print("this will only be executed if user typed smth OTHER THAN : LEVEL2_OPTION1 or LEVEL2_OPTION2")
elif answer1.lower() == "answer2":
    print("this will only be executed if user said 'ANSWER2' on level 1") 
else:
    # in case user answered with smth completely different on level 1
    print("this will only be executed if user typed smth different")