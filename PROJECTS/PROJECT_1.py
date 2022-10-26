#Aim : To build a Rock_Paper_Scissors game Using Python with my knowledge(No cheating!)
import random as r
Possible_Results = ["Rock", "Paper", "Scissors"]

def rock_paper_scissors(user_answer):
    user_points = 0

    computer_answer = r.choice(Possible_Results)

    if computer_answer == user_answer:
        print("DRAW")
    else:

        if computer_answer == "Rock" and user_answer == "Paper":
            print("Computer Wins")
        elif computer_answer == "Rock" and user_answer == "Scissors":
            print("You Win!")
            user_points += 1
        else:

           if computer_answer == "Paper" and user_answer == "Rock":
              print("Computer Wins!")
           elif computer_answer == "Paper" and user_answer == "Scissors":
              print("You Win!")
              user_points += 1
           else:

              if computer_answer == "Scissors" and user_answer == "Rock":
                 print("You Win!")
                 user_points += 1
              elif computer_answer == "Scissors" and user_answer == "Paper":
                 print("Computer Wins!")
                 print("Your Score:", user_points)

print(rock_paper_scissors(r.choice(Possible_Results)))
    
    
    

    



    
    
    
    

    
