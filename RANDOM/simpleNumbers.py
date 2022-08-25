def isprime(num):
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return "Сложное"
    return "Простое"

user_number = (input("Введите число: "))
print(isprime(user_number))