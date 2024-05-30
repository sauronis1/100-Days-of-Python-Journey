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

#Write your code below this line 👇
import random

#obrázky list
images = [rock, paper, scissors]
#choices + printim obrazek toho co si vybral hráč a počítač
player_choice = int(input("What are you going to play? Type (0) for ROCK, (1) for PAPER, (2) for SCISSORS. "))
if player_choice >=3 or player_choice < 0:
    print("Invalid number mate.")
else:
    print(images[player_choice])
                                        #if player_choice == 0:
                                        #    print(rock)
                                        #elif player_choice == 1:
                                        #    print(paper)
                                        #else:
                                        #    print(scissors)
                                            
    computer_choice = random.randint(0, 2)
    print("The computer chose:")
    print(images[computer_choice])
                                        #if computer_choice == 0:
                                        #    print(rock)
                                        #elif computer_choice == 1:
                                        #    print(paper)
                                        #else:
                                        #    print(scissors)
    
    #zaznamenání voleb do listu, computer choice jde první.
    game = []
    game.append(computer_choice)
    game.append(player_choice)
    
    #if gaming
    if game[0] == game [1]:
        print("It's a draw.")
    elif (game[0] == 0 and game[1] == 1) or (game[0] == 1 and game[1] == 2) or (game[0] == 2 and game[1] == 0):
        print("You win!")
    else:
        print("You lose.")
        
