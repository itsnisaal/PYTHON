
# Simple Calculator - Class 10 Project

while True:
    print("\n----- CALCULATOR -----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus (Remainder)")
    print("6. Power (a^b)")
    print("7. Square Root of a number")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 8:
        print("Exiting the calculator. Goodbye!")
        break

    if choice in (1, 2, 3, 4, 5, 6):
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if choice == 1:
            print("Result: ", a + b)
        elif choice == 2:
            print("Result: ", a - b)
        elif choice == 3:
            print("Result: ", a * b)
        elif choice == 4:
            if b != 0:
                print("Result: ", a / b)
            else:
                print("Error: Division by zero is not allowed.")
        elif choice == 5:
            if b != 0:
                print("Result: ", a % b)
            else:
                print("Error: Modulus by zero is not allowed.")
        elif choice == 6:
            print("Result: ", a ** b)

    elif choice == 7:
        num = int(input("Enter a number: "))
        if num >= 0:
            print("Result: ", num ** 0.5)
        else:
            print("Error: Cannot find square root of a negative number.")

    else:
        print("Invalid choice! Please try again.")