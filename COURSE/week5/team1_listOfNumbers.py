numbers = []
number = -1

while number != 0:
    number = int(input("Enter a list of numbers, type 0 when finished: "))
    if number != 0:
        numbers.append(number)

sum = sum(numbers)
average = sum / len(numbers)
largest = max(numbers)
smallest = min(i for i in numbers if i > 0)
sort = sorted(numbers)
print(f"""
The sum is: {sum}
The average is: {average}
The largest number is: {largest}
The smallest positive number is: {smallest}
The sorted list is: {sort}
""")