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

# correct_password = 12345
# user_password = float(input("Enter the password: "))
# trial = 1
  
# while user_password != correct_password and trial < 5:
#     print("Incorrect password! try again.")  
#     trial += 1
#     user_password = float(input("Enter the password: "))
# if user_password == correct_password:
#     print("Your'e logged in to the system.")
# else:
#     print("Your'e kicked off from the system.")


# scores = int(input("Enter any test scores: "))
# count = 0
# scores_A = 0
# sum  = 0

# while count >= 0:
#     if count >= 90:
#         count += 1

    
#     scores = int(input("Enter any test scores(negative to stop): "))
#     count += 1 

# if scores >= 0:
#     print(f"Number of A's (90 or above): {a_count}")


# score = int(input("Enter a score: "))
# count = 0
# score_A = 0
# sum = 0

# while score >= 0:
#     if score >= 90:
#         score_A += 1
    
    # sum += score
    # count += 1
    # score = int(input("Enter a score (Negative number to stop): "))
    

# if count > 0:
#     print("Total number of A's is ", score_A)
#     print("The sum is", sum)
#     average = sum/count
#     print("The average is ", average)
# else:
#     print("Invalid values")


# import random

# score = random.randint(1, 100)
# guesses_left = 5

# while guesses_left > 0:
#     if guesses_left == 1:
#         print("You have 1 guess left.")
#     else:
#         print(f"You have {guesses_left} guesses left")

#     guess = int(input("Enter your guess: "))

#     if guess == score:
#         print("correct! you win!")

#     elif guess < score:
#         print("Higher!")
#     else:
#         print("lower!")
#     if guesses_left == 0:
#         print("Out of guesses! the number was", score)

import random

secret = random.randint(1, 100)
guesses_left = 7

while guesses_left > 0:
    if guesses_left == 1:
        print("You have 1 guess left.")
    else:
        print(f"You have {guesses_left} guesses left.")

    guess = int(input("Enter your guess: "))

    if guess == secret:
        print("Correct! You win!")
        break
    elif guess < secret:
        print("Higher!")
    else:
        print("Lower!")

    guesses_left -= 1

if guesses_left == 0:
    print(f"Out of guesses! The number was {secret}.")



