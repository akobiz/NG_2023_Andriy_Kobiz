books = {
    "NAME": ["UNKNOWN", "In Search of Lost Time", "Example", "example"],
    "AUTHOR": ["NO AUTHOR","Marcel Proust", "Example", "Example"],
    "PAGES": ["0", "4215", "1337", "1337"],
    "GENRE": ["NO GENRE", "Modernist", "Drama", "Feshn"],
    "BINDING": ["NO BINDING", "Hard", "Hard", "Soft"]
}

def askChoice():
    print("1.Add book\n2.Delete book\n3.Change parameters in book\n"
          "4.Find book\n5.Show library\nAny other symbol to exit")
    return input('Choose an operation: ')

def addBook():
    for key in books.keys():
        books[key].append(input(f'{key}: '))
    print("Succesfully added.")

def takeBookIndex():
    for book in books["NAME"]:
        print(str(books["NAME"].index(book)) + ": \"" + book + "\"")
    return int(input('Choose book index: '))

def deleteBook():
    index = takeBookIndex()
    for key in books.keys():
        books[key].remove(books[key][index])
    print("Succesfully deleted.")

def changeParameters():
    index = takeBookIndex()
    for key in books.keys():
        print(key)
        if key == list(books.keys())[-1]:
            parameter = input('Enter parameter to change: ').upper()
            books[parameter][index] = input(f'Change {parameter}: ')
            print("Succesfully changed.")

def findBook():
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

def showLibrary():
    for value in range(len(books["NAME"])):
        print("=========\n")
        for key in books.keys():
            print(str(key) + ": " + str(books[key][value]))
    print("===============\n\n")

def chooseOperation():
    while(True):
        match(askChoice()):
            case "1": addBook()
            case "2": deleteBook()
            case "3": changeParameters()
            case "4": findBook()
            case "5": showLibrary()
            case _: return False

def main():    
    chooseOperation()

if __name__ == "__main__":
    main()