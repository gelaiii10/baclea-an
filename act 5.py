positive_integer = int (input ("Enter a positive number: "))
n = positive_integer 
factorial = 1

while positive_integer < 0 :
    print ("Not a positive number. ")
    positive_integer = int (input ("Enter a positive number: "))
    n = positive_integer
    
for i in range (1,positive_integer) :
    positive_integer *= i
    factorial = positive_integer 

print ("The factorial of", n, "is:", factorial)