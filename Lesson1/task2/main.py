print("Enter two numbers: ")
first, second = int(input()), int(input())

print("1.Add two numbers\n2.Minus two numbers\n3.Multiply two numbers\n"
      "4.Divide two numbers")

match(int(input("Choose an operation"))):
    case 1: print(first + second)
    case 2: print(first - second)
    case 3: print(first * second)
    case 4: print(first / second)
    case _: print("Unknown operation number...")