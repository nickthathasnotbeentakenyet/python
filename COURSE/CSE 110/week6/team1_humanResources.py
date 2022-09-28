with open("./week6/hr_system.txt") as file:
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


# with open("./кадры.txt", encoding='utf-8') as файл:
#     print("Выписка из бухгалтерии: \n" + '-'*23)
#     for строка in файл: 
#         строка.strip()
#         строка = строка.split()
#         зарплата = float(строка[3]) / 24
#         if строка[2] == "Инженер":
#             зарплата += 1000
#         print(f"{строка[0]:<12} (ID: {строка[1]:<4}), {строка[2]:<12} - {зарплата:.2f} ₽")