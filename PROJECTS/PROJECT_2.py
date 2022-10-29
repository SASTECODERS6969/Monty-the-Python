#Aim : To make a guessing game
import random as r
user_answer = int(input("Enter a number from 1 to 30"))
if 0 < user_answer < 10:
    def guessing(user_answer):
        a = r.randrange(1, 10)
        if a == user_answer:
            print("You guessed the Number correct! The Number was", a)
        else:
            print("Sorry! you're guess was wrong. The Number was", a)

    guessing(user_answer)

if user_answer > 10:
    print("Please give a number less than 10")
elif user_answer < 0:
    print("Please give a number more than 1 and less than 10")

