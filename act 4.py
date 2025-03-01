print("1. addition(+)")
print("2. subtraction(-)")
print("3. multiplication(*)")
print("4. division(/)")
print("5. exit")

def calculator ():
    while 1<=5:
        operation = int(input("Choose an operation 1-5: "))
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter first number: "))
        if operation == '5':
            print("Goodbye!")
        elif operation == '1':
            sum = num1 + num2
            print("result", sum)
        elif operation == '2':
            difference = num1 - num2 
            print("result", difference)
        elif operation == '3':
            product = num1 * num2
            print("result", product)
        elif operation == '4':
            quotient = num1 / num2
            print("result", quotient)
        else:
            print("Invalid choice! Please select a valid option.")
                        