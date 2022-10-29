#Aim : To make a guessing game
import random as r
user_answer = int(input("Enter a number from 1 to 30"))

def guessing(user_answer):
    a = r.randrange(1, 30)
    if a == user_answer:
        print("You guessed the Number correct! The Number was", a)
    else:
        print("Sorry! you're guess was wrong. The Number was", a)

guessing(user_answer)
