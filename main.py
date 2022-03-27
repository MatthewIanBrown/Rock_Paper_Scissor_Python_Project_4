rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



#Geeting the Players input
print("Want to play Rock Papers Scissors?")
players_choice = (input('Please choice "Rock", "Paper", or "Scissors"\n')).lower()


#Random Output for Opponent
import random
rock_paper_scissors=["Rock","Paper","Scissors"]
computer_choice=(random.choice(rock_paper_scissors)).lower()

#Setting the Rules/outcome


if players_choice== "rock" and computer_choice == "scissors":
  print(f"\n Player Wins - You played {players_choice}, and the computer played {computer_choice}. \n {rock} \n BEATS\n {scissors}" )

elif players_choice== "scissors" and computer_choice == "paper":
  print(f"\n Player Wins - You played {players_choice}, and the computer played {computer_choice}. \n {scissors} \n BEATS\n {paper}" )

elif players_choice== "paper" and computer_choice == "rock":
  print(f"\n Player Wins - You played {players_choice}, and the computer played {computer_choice}. \n {paper} \n BEATS\n {rock}" )  
  
elif players_choice== computer_choice :
  print(f"\n Player and Computer picked the same \n -----You Tied-----\n You played {players_choice}, and the computer played {computer_choice}." )

else:
  print(f"\n Computer Wins\n You played {players_choice}, and the computer played {computer_choice}.")

