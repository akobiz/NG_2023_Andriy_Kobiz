books = {
    "NAME": ["UNKNOWN", "In Search of Lost Time", "Example", "example"],
    "AUTHOR": ["NO AUTHOR","Marcel Proust", "Example", "Example"],
    "PAGES": ["0", "4215", "1337", "1337"],
    "GENRE": ["NO GENRE", "Modernist", "Drama", "Feshn"],
    "BINDING": ["NO BINDING", "Hard", "Hard", "Soft"]
}

while(True):
    print("1.Add book\n2.Delete book\n3.Change parameters in book\n4.Find book\n5.Show library")

    choice = int(input())
    match(choice):
        case 1:
            for key in books.keys():
                books[key].append(input(f'{key}: '))
            print("Succesfully added.")
        case 2:
            for book in books["NAME"]:
                print(str(books["NAME"].index(book)) + ": \"" + book + "\"")
            index = int(input('Choose book index: '))
            for key in books.keys():
                books[key].remove(books[key][index])
            print("Succesfully deleted.")
        case 3:
            for book in books["NAME"]:
                print(str(books["NAME"].index(book)) + ": \"" + book + "\"")
            index = int(input('Choose book index: '))
            for key in books.keys():
                print(key)
                if key == list(books.keys())[-1]:
                    parameter = input('Enter parameter to change: ').upper()
                    books[parameter][index] = input(f'Change {parameter}: ')
                    print("Succesfully changed.")
        case 4:
            findBy = input(f'Find book by {list(books.keys())}: ').upper()
            findBook = None
            booksCopy = books.copy()
            while(findBook != 'e'):
                findBook = input(f'Enter {findBy} to search(\'e\' to stop): ')
                if findBook in booksCopy[findBy]:
                    index = booksCopy[findBy].index(findBook)
                    print("================\n")
                    for key in booksCopy.keys():
                        print(f"{key}: {booksCopy[key][index]}")
                        del booksCopy[key][index]
                else: print("Not found. Try again...")
        case 5: 
            for value in range(len(books["NAME"])):
                print("=========\n")
                for key in books.keys():
                    print(str(key) + ": " + str(books[key][value]))
        case _:
            break