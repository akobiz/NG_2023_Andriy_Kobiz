length = int(input('Enter the length of the text, or numbers you\'ll be entering: '))

while(True):
    userSomething = input(f"Enter text or numbers with length {length}: ")
    if len(userSomething) == length:
        element = userSomething.count(input('Enter element to count him:'))
        print(f"Element count of you asked in your list = {element}")
        break
