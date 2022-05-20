with open("C:/Users/warning/Downloads/hr_system.txt") as file:
    for line in file: 
        line = line.split()
        id = line[1]
        salary = float(line[3])
        paycheck = salary / 12 / 2
        bonus = 0
        if line[2] == "Engineer":
            bonus = 1000
        total = paycheck + bonus
        print(f"{line[0]} (ID: {id}), {line[2]} - ${total:.2f}")
