user_name = input ("Set your login username: ")
user_password = input ("Set your password: ")


attempts = 0
max_attempts = 3


while attempts < max_attempts:
   enter_name = input("Enter Username: ")
   enter_password = input("Enter Username: ")


   if enter_name == user_name and enter_password == user_password:
       print("Login Successful.")
   else:
       attempts += 1
       if attempts < max_attempts:
           print ("Incorrect username or password. Try again.")
       else:
           print("Too many failed attempts. Access denied.")