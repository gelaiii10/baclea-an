print("Simple Calculator")
print("1: Addition(+)")
print("2: Subtraction(-)")
print("3: Multiplication(*)")
print("4: Division(/)")
print("5: Exit")
print("Choose an operation(1-5): ")
operation = float(input()) 

while operation >= 1 or operation <= 5:
    if operation == 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1, "+", num2, "=", num1 + num2)
        print("Simple Calculator")
        print("Choose an operation(1-5): ")
        operation = float(input())
    elif operation == 2:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1, "-", num2, "=", num1 - num2)
        print("Simple Calculator")
        print("Choose an operation(1-5): ")
        operation = float(input())
    elif operation == 3:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1, "*", num2, "=", num1 * num2)
        print("Simple Calculator") 
        print("Choose an operation(1-5): ")
        operation = float(input())
    elif operation == 4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            print("Result:", num1, "/", num2, "=", num1 / num2)
        else:
            print("Cannot divide by zero.")
            
        print("Simple Calculator") 
        print("Choose an operation(1-5): ")
        operation = float(input())
    elif operation == 5:
        print("Goodbye!")
        
    else:
        print("Invalid Entry.") 
        print("Choose an operation(1-5): ")
        operation = float(input())