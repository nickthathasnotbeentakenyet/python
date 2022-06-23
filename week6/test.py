path = "./week6/life-expectancy.csv"
choice = int(input("\nEnter the year of interest: "))
sum_all = 0
avg_all = 0
i = 0
c_year = 0
c_max_life = 0
c_max_country = ""
with open(path) as file:
    # skipping first line
    next(file)
    for line in file: 
        line = line.strip()
        line = line.split(",")
        # defining some variables
        countries = line[0]
        year = int(line[2])
        life = float(line[3])
        if choice == year:
            if life > c_max_life:
                # next three variables will be updated only for the greatest value for life, which is line[3]
                c_year = choice
                c_max_life = life
                c_max_country = countries   
            # count and sum will be incrementing each time the years match, not when life > c_max_life only
            i += 1
            sum_all += life           
            avg_all = sum_all / i
print(f"For year {c_year} Average: {avg_all:.2f}")
