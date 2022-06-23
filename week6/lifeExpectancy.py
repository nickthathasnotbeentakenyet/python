# path = input("Type path to the file: ")
path = "./week6/life-expectancy.csv"
year = input("\nEnter the year of interest: ")
user_country = input("Enter the country of interest: ")
overall_max, overall_min = 0, 2**10
spec_year_max, spec_year_min = 0, 2**10
user_max, user_min = 0, 2**10
country_exists = False
count = 0
user_total = 0
user_count = 0
expectancy_list = []

with open(path) as file:
    # skiiping the first line in the file . Though, I am using another method below
    # file = file.readlines()
    # for line in file[1:]:
    for line in file: 
        line = line.strip()
        line = line.split(",")
        # skipping the first line in the file
        if line[3] == "Life expectancy (years)":
            continue
        # finding overall maximums 
        if float(line[3]) > overall_max:
            overall_max = float(line[3])
            overall_country_max = line[0]
            overall_year_max = line[2]
        # finding overall minimums
        if float(line[3]) < overall_min:
            overall_min = float(line[3])
            overall_country_min = line[0]
            overall_year_min = line[2]
        # finding info for a specific year
        if line[2] == year:
            count += 1
            expectancy_list.append(line[3])
            if float(line[3]) > spec_year_max:
                spec_year_max = float(line[3])
                spec_year_country_max = line[0]
            if float(line[3]) < spec_year_min:
                spec_year_min = float(line[3])
                spec_year_country_min = line[0] 
        # finding info for a specific country
        if line[0] == user_country:
            country_exists = True
            user_count += 1
            user_total += float(line[3])
            if float(line[3]) > user_max:
                user_max = float(line[3])
                user_year_max = line[2]
            if float(line[3]) < user_min:
                user_min = float(line[3])
                user_year_min = line[2]
    # finding sum to calculate average 
    total = 0
    for i in expectancy_list:
        total += float(i)    
    # printing overalls 
    print(f"\nThe overall max life expectancy is: {overall_max:.2f} from {overall_country_max} in {overall_year_max}")
    print(f"The overall min life expectancy is: {overall_min:.2f} from {overall_country_min} in {overall_year_min}")
    print(f"\nFor the year {year}:")
    # dealing with the division by zero error
    if not expectancy_list:
        print("No information found for this year\n")
    # calculating average and printing results for a specific year
    else:    
        spec_year_average = total / count 
        print(f"The average life expectancy across all countries was {spec_year_average:.2f}")
        print(f"The max life expectancy was in {spec_year_country_max} with {spec_year_max:.2f}")
        print(f"The min life expectancy was in {spec_year_country_min} with {spec_year_min:.2f}\n")
    # printing results for a specific country
    print(f"For the country of your interest [{user_country}]:")
    if country_exists:
        user_avg = user_total / user_count
        print(f"The max life expectancy was {user_max:.2f} in {user_year_max}")
        print(f"The min life expectancy was {user_min:.2f} in {user_year_min}")
        print(f"The average life expectancy was {user_avg:.2f}\n")
    else:
        print(f"Sorry, no information found for {user_country}. Please varify the name.\n")    
