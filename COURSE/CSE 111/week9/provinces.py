def main():
    file_list = []
    count = 0
    with open("COURSE\CSE 111\week9\provinces.txt") as file:
        for line in file:  
            line.split('\n')
            line = line.strip()
            file_list.append(line)
    print(file_list)
    file_list.pop(0)
    file_list.pop()
    for _ in range(len(file_list)):
        if file_list[_] == "AB":
            file_list[_] = "Alberta"
    # посчитать сколько раз встречается слово
    count = file_list.count("Alberta")
    print(f"Alberta Count: {count}")
    print(file_list)

if __name__ == "__main__":
    main()