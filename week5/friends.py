friends = []
name = ""

while name != "end":
    name = input("Type the name of a friend: ")
    if name != "end":
        friends.append(name)
print(f"Your friends are: {friends}")
