with open("./week6/books.txt") as books:
    for line in books:
        line = line.strip()
        print(line)


# нумератор = 1
# with open("./книги.txt", encoding="utf-8") as книги:
#     файл = книги.readlines()
#     файл.reverse()
#     for номер, строка in enumerate(файл):
#         строка = строка.strip()
#         if номер == 8:
#             continue
#         print(f"{нумератор}. {строка}")
#         нумератор += 1