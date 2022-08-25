from random import randint


class Animal:
    def __init__(self, name, color, legs, hands, tail):
        self.name = name
        self.color = color
        self.legs = legs
        self.hands = hands
        self.tail = tail
    
    def speak(self):
        print("рррр")

class Dog(Animal):
    def speak(self):
        print("гав")
class Cat(Animal):
    def speak(self):
        return "мяу"
class human(Animal):
    def speak(self):
        print("Привет, меня зовут", self.name)
    def mind(self):
        return randint(1,100)

имя = input("Дайте имя персонажу: ")
цвет = input("Цвет глаз: ")
имя_кошки= input ("дайте имя кошке: ")
кошка_пользователя = Cat(имя_кошки, 'ginger', 2,2,True)
персонаж_пользователя = human(имя,цвет, 2, 2, False)
персонаж_пользователя.speak()
print(f"У меня {персонаж_пользователя.hands} руки")
print("Мой мозг загружен на ", персонаж_пользователя.mind(), "%")
print("Мою кошку зовут ", имя_кошки, "она умеет говорить: ", кошка_пользователя.speak())