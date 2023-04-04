length = int(input('Enter length of something: '))

while(True):
    userSomething = input(f"Enter something with length {length}: ")
    if len(userSomething) == length:
        element = userSomething.count(input('Enter element to count him:'))
        print(f"Element count of you asked in your list = {element}")
        break
