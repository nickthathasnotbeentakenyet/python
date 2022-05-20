def display_regular(message):
    return message
def display_uppercase(message):
    return message.upper()
def display_lowercase(message):
    return message.lower()

message = input("What is your message?: ")
print(display_regular(message) +"\n"\
         + display_uppercase(message)+"\n"\
            + display_lowercase(message))