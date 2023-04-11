def drawRhombus(size = 10, temp = 1):
    print(" " * size + "*" * temp*2)
    if size > 1:
        drawRhombus(size - 1, temp + 1)
    print(" " * size + "*" * temp*2)

drawRhombus(45)