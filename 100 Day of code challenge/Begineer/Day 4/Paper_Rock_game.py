import random

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

game_imagies = [rock, paper, scissors]

player_choise = int(input("Please enter your choise by type 0 for 'rock', 1 for 'paper' or 2 for 'scissors'\n:  "))
if player_choise >= 3 or player_choise < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_imagies[player_choise])

    computer_choise = random.randint(0, 2)
    print(f"Computer choise")
    print(game_imagies[computer_choise])

    if player_choise == 1 and computer_choise == 2:
        print("You wins!")
    elif computer_choise == 0 and player_choise == 2:
        print("You lose!")
    elif computer_choise > player_choise:
        print("You lose!")
    elif player_choise > computer_choise:
        print("You win!")
    elif computer_choise == player_choise:
        print("It's a draw")

