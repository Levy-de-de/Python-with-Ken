# # question 1
# # for _ in range(4):
# #     print("*" * 19)

# #    question 2
# # print("*" * 20)
# # for _ in range(2):
# #     print("*" + " " * 18 +"*")
# # print("*" * 20)

# # question 3
# # print("*")
# # print("*" * 2)
# # print("*" * 3)
# # print("*" * 4)

# # question 4
# # numerator = 512 - 282
# # denominator = 47 * 48 + 5
# # result = numerator / denominator
# # print(result)

# # question 5
# # num = float(input("Enter a number: "))
# # square = num ** 2

# # print("The square of", num, "is", square, ".", sep=" ")

# # question 6
# # x = float(input("Enter a numberr x:"))
# # print(x, 2*x, 3*x, 4*x , 5*x, sep="---")

# # question 7
# # kg = float(input("Enter your weight in kg:"))
# # pounds = kg * 2.2

# # print("You weigh", pounds, "pounds.")
 
# # #  question 8
# # num1 = float(input("Enter your first number:"))
# # num2 = float(input("Enter your second number:"))
# # num3 = float(input("Enter your third number:"))

# # total = num1 + num2 + num3
# # average = total / 3

# # print("Total:", total)
# # print("Average", average)

# # question 9

# # meal_price = float(input("Enter the price of the meal: "))
# # tip_percent = float(input("Enter the tip percentage you want to leave: "))

# # tip_amount = meal_price * (tip_percent / 100)
# # total_bill = meal_price + tip_amount

# # print("Tip amount:", tip_amount)
# # print("Total bill with tip:", total_bill)


# import random
# for _ in range(50):
#     print(random.randint(3, 6))

# import random
# x = random.randint(1, 50)
# y = random.randint(2, 5)
# result = x ** y
# print(f"x = {x}, y = {y}, x^y = {result}")

# import random

# n = random.randint(1, 10)

# for _ in range(n):
#     print("Levy")


# x = float(input("Enter the first number (x): "))
# y = float(input("Enter the second number (y): "))

# difference = abs(x - y)

# print(f"|x - y| = {difference}")


# # Program to convert seconds into minutes and seconds

# # Ask the user for a number of seconds
# seconds = int(input("Enter the number of seconds: "))

# # Compute minutes and remaining seconds
# minutes = seconds // 60
# remaining_seconds = seconds % 60

# # Display the result
# print(f"{seconds} seconds is {minutes} minutes and {remaining_seconds} seconds.")


# # Program to compute future hour on a 12-hour clock

# # Ask the user for the current hour (1–12)
# current_hour = int(input("Enter the current hour (1-12): "))

# # Ask how many hours into the future
# hours_ahead = int(input("Enter how many hours into the future: "))

# # Compute the future hour using modular arithmetic
# future_hour = (current_hour + hours_ahead) % 12

# # Adjust so that 0 becomes 12 (since we’re using a 12-hour clock)
# if future_hour == 0:
#     future_hour = 12

# print(f"In {hours_ahead} hours, it will be {future_hour} o'clock.")
   





# power = int(input("Enter a power: "))
# last_digit = pow(2, power, 10)  # mod 10
# print(f"The last digit of 2^{power} is {last_digit}")


# power = int(input("Enter a power: "))
# last_two_digits = pow(2, power, 100)  # mod 100
# print(f"The last two digits of 2^{power} are {last_two_digits:02d}")

# power = int(input("Enter a power: "))
# digits = int(input("How many digits do you want? "))
# modulus = 10 ** digits
# last_digits = pow(2, power, modulus)
# print(f"The last {digits} digits of 2^{power} are {last_digits:0{digits}d}")
