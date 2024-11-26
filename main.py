print("I can solve ax^2 + bx + c = 0 for you!")

while True:
    try:
        # Input coefficients
        a = float(input("Please give me the 'a' coefficient: "))
        if a == 0:
            print("Sorry, but 'a' cannot be zero.")
            continue

        b = float(input("Please give me the 'b' coefficient: "))
        c = float(input("Please give me the 'c' coefficient: "))

        # Calculate delta
        delta = b**2 - 4*a*c
        if delta < 0:
            print("Sorry, but that quadratic does not have real roots.")
            continue

        print("Thank you, that is a valid input :) OKAY I'LL SOLVE IT NOW.")
        break  # Valid input received, exit loop

    except ValueError:
        print("That is not a real number!")

# Solve and display roots
if delta > 0:
    root1 = (-b - delta**0.5) / (2 * a)
    root2 = (-b + delta**0.5) / (2 * a)
    print("Root 1:", root1)
    print("Root 2:", root2)
else:
    root = -b / (2 * a)
    print("Root:", root)

# Quit
quit()