def main():

    person_variable = person_do_smth(person, do)
    print(person_variable)

    # person_variable = person_do_smth(person='Jake',do='sing')
    # print(person_variable)

    # name = 'Jake'
    # person_variable = person_do_smth(person=name,do='sing')
    # print(person_variable)

    # names = ['Jake','Mike','Tony']
    # for name in names:
    #     person_variable = person_do_smth(person=name,do='sing')
    #     print(person_variable)

    # person_action_dictionary = {
    #     'Mike' : ['sing','work','pray'],
    #     'Jake' : ['jog','swim']
    # }
    # for key,value in person_action_dictionary.items():
    #     person_name = key
    #     person_actions = value
    #     for action in person_actions:
    #         person_variable = person_do_smth(person=person_name,do=action)
    #         print(person_variable)

    # person_variable1 = person_do_smth(person='Jake', do='sing')
    # person_variable2 = person_do_smth(do='sing', person='Jake')
    # print(person_variable1)
    # print(person_variable2)

    # person_variable = person_do_smth('Jake', 'sing')
    # print(person_variable)

    # person_variable = person_do_smth('sing', 'Jake')
    # print(person_variable)

def person_do_smth(person, do):
    return f"{person} is {do}ing"


if __name__ == '__main__':
    main()
