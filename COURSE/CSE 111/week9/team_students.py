import csv

I_NUMBER = 0
NAME = 1
PATH = "COURSE/CSE 111/week9/students.csv"
dictionary = {}

def main():
    student_i_number = input("Please enter an I-Number (xxxxxxxxx): ")

    # call function to purify the number
    student_i_number = clean_number(student_i_number)

    # call function to check for characters other than digits or dashes
    check_valid(student_i_number)

    # call function to find a match
    students_table = read_dict(PATH, I_NUMBER)
    if student_i_number in students_table : 
        print(students_table[student_i_number][NAME])
    else: print("No such student")


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    with open(filename, "rt") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            key = line[key_column_index]
            dictionary[key] = line

    return dictionary


def clean_number(student_i_number):
    # dealing with dashes
    clean_number = ''
    for _ in range(len(student_i_number)):
        if student_i_number[_] == '-': clean_number += ''
        else: clean_number += student_i_number[_]
    return clean_number

def check_valid(student_i_number):
    for _ in student_i_number:
        if str(_).isdigit(): pass
        else: print("Invalid I-Number"),exit(0)
    if len(student_i_number) < 9: 
        print("Invalid I-Number: too few digits"),exit(0)
    if len(student_i_number) > 9:
        print("Invalid I-Number: too many digits"),exit(0)
            
if __name__ == '__main__':
    main()
