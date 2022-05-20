'''
# TODO: CORE REQUIREMENTS
Open the file, read through it line by line, separate the line into the appropriate pieces and display each book in this format:
Scripture: Old Testament, Book: Genesis, Chapters: 50
Find the largest number of chapters in the scriptures.
Find the book that has the largest number of chapters in the scriptures.
# TODO: STRETCH CHALLENGE
Change your program so that it only prints the books in the Book of Mormon.
Find the book in the Book of Mormon that has the largest number of chapters.
At the beginning of the program, ask the user which volume of scriptures they would like to learn about 
(for example, Old Testament, New Testament, Book of Mormon, Doctrine and Covenants, Pearl of Great Price). 
Then, find the book in that volume of scripture that has the largest number of chapters.
#NOTE: Genesis:50:Old Testament
'''
largest = 0
largest_BOM = 0
user_book = input("Which volume of scriptures you would like to learn about: ")
largest_user = 0
with open('./week6/books_and_chapters.txt') as file:
    for line in file:
        line = line.strip()
        line = line.split(":")
        # COMMENT: display each book in this format
        # print(f"Scripture: {line[2]}, Book: {line[0]}, Chapters: {line[1]}")
        if int(line[1]) > largest:
            largest = int(line[1])
            book = line[0]
        # COMMENT: STRETCH STARTS HERE
        if line[2] == "Book of Mormon":
            # print(line[0])
            if int(line[1]) > largest_BOM:
                largest_BOM = int(line[1])
                book_BOM = line[0]
        if line[2] == user_book:
            if int(line[1]) > largest_user:
                largest_user = int(line[1])
                book_user = line[0]
# COMMENT: Find the largest number of chapters in the scriptures AND Find the book
print(f"The largest book is {book}. It has {largest} chapters")
# COMMENT: Find the book in the Book of Mormon that has the largest number of chapters. 
print(f"The largest book in the Book of Mormon is {book_BOM}. It has {largest_BOM} chapters")
# COMMENT: User book
print(f"The largest book in the {user_book} is {book_user}. It has {largest_user} chapters")
