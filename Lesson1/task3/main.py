from math import sqrt

print("Enter a, b, c to fill quadratic equation(ax^2 + bx + c = 0)")
userA, userB, userC = int(input("a = ")), int(input("b = ")), int(input("c = "))

discriminator = (userB**2) + (4 * userA * userC)

if discriminator < 0:
    print("No roots.")
else:
    discriminator = sqrt(discriminator)
    print(f"D = {discriminator}")
    if discriminator > 0:
        firstRoot = (-userB + discriminator) / (2 * userA)
        secondRoot = (-userB - discriminator) / (2 * userA)
    else:
        firstRoot = (-userB + discriminator) / (2 * userA)
        secondRoot = "No root."
    print(f"x1 = {firstRoot}, x2 = {secondRoot}")