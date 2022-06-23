with open("C:/Users/warning/Downloads/hr_system.txt") as file:
    for line in file: 
        line.strip()
        line = line.split()
        name = line[0]
        id = line[1]
        job_title = line[2]
        salary = float(line[3])
        paycheck = salary / 24
        if line[2] == "Engineer":
            paycheck = paycheck + 1000
        print(f"{name} (ID: {id}), {job_title} - ${paycheck:.2f}")
