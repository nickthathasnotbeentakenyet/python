from posixpath import split


people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
youngest = 2**10
for person in people:
    person = person.split(" ") 
    if int(person[1]) < youngest:
        youngest = int(person[1])
        name = person[0]
print(f"{name} is the youngest being {youngest} years old")