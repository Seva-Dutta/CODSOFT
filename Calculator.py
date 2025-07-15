while True:
    print("\n--- Simple Calculator ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    match choice:
        case '1':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("\nResult:" ,a, "+" ,b, "=" ,a + b)
        case '2':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("\nResult:" ,a, "-" ,b, "=" ,a - b)
        case '3':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("\nResult:" ,a, "*" ,b, "=" ,a * b)
        case '4':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if b != 0:
                print("\nResult:" ,a, "/" ,b, "=" ,a / b)
            else:
                print("Error: Division by zero is not allowed.")
        case '5':
            print("Exiting the calculator.")
            break
        case _:
            print("Invalid choice. Please select a valid option.")

    


             
