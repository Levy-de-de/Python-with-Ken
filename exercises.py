# i = 1
# while i < 51:
#     print(i)
#     i += 1 


# x= "Hello world"
# i = 0
 
# while i < len(x):
#     print(x[i])
#     i += 2

# kg  = float(input("Enter a weight: "))
# while kg  < 0:
#     print("Invalid")
#     kg  = float(input("Enter a weight: "))
# pounds = kg * 2.20462262
# print("Your wight is: ", pounds, "pounds")

correct_password = 12345
user_password = float(input("Enter the password: "))
trial = 1
  
while user_password != correct_password and trial < 5:
    print("Incorrect password! try again.")  
    trial += 1
    user_password = float(input("Enter the password: "))
if user_password == correct_password:
    print("Your'e logged in to the system.")
else:
    print("Your'e kicked off from the system.")


