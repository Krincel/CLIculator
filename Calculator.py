def add(x, y):
    return x + y 
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y
def power(x, y):
     return x ** y

while True:
    print("\nSimple Calculator")
    print("Please select an operation:")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Power")
    print("6: Exit Program")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice == "6":
        print("Goodbye!\nExiting program...")
        break
    
    if choice in ("1", "2", "3", "4", "5"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue
    
    if choice == "1": 
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == "2":
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == "3":
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == "4":
        try:
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        except ValueError as e:
            print(e)
    elif choice == "5":
        try:
            print(f"{num1} ** {num2} = {power(num1, num2)}")
        except ValueError as undefined:
            print(undefined)
    else:
        print("Invalid choice! Please try again.")
