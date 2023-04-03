length = int(input('Enter length of input: '))

while(True):
    userInput = input('Enter something: ')
    if len(userInput) == length: 
        print("You've entered correct length something!")
        break
    print(f"Oops... Length of your input is {len(userInput)}, you asked for " 
          f"{length} length. So the difference = {length - len(userInput)}")