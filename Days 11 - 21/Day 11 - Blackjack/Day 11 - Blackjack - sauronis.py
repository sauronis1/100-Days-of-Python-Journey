def computer_round():
  while players["Computer"][1] < 17:
    print("The computer draws a card...")
    print()
    players["Computer"][0].append(random.choice(cards))
    count_scores(players)
    if players["Computer"][1] > 21:
      if 11 in players["Computer"][0]:
        location_of_11 = players["Computer"][0].index(11)
        players["Computer"][0][location_of_11] = 1
        count_scores(players) 

def evaluate_input(prompt):
  print_final_scores()
  print(prompt)
  print()
  play = False

def evaluate():
  if players["Computer"][1] > 21:
    evaluate_input("The dealer went over 21. You win.")
  elif players["Computer"][1] == players["Player"][1]:
    evaluate_input("It's a draw!")
  elif players["Computer"][1] > players["Player"][1]:
    evaluate_input("The dealer wins. You lose.")
  elif players["Player"][1] > players["Computer"][1] and players["Player"][1] <=21:
    evaluate_input("You win!")

def count_scores(players):
  current_score_player = sum(players["Player"][0])
  current_score_computer = sum(players["Computer"][0])
  players["Player"][1] = current_score_player
  players["Computer"][1] = current_score_computer


def draw_one_card():
  one_card = True
  while one_card:
    one_card_question = input("  Type 'y' to draw another card, type 'n' to pass: ")
    print()
    
    if one_card_question == "y":
      players["Player"][0].append(random.choice(cards))
      one_card = True
      count_scores(players)
      if players["Player"][1] > 21:
        if 11 in players["Player"][0]:
          location_of_11 = players["Player"][0].index(11)
          players["Player"][0][location_of_11] = 1
          count_scores(players) 
          print_scores()
        else:
          print_scores()
          print("You've gone over 21. You lose.")
          print()
          one_card = False
          play = False
      else:
        print_scores()
      #check whether the player hasn't gone over 21
    elif one_card_question == "n":
      computer_round()
      one_card = False


def print_scores():
  print("Your cards: " + str(players["Player"][0]) + ", current score: " + str(players["Player"][1]))
  print("Computer's first card: " + str(players["Computer"][0][0]))
  print()

def print_final_scores():
  print("Your cards: " + str(players["Player"][0]) + ", current score: " + str(players["Player"][1]))
  print("Computer's final hand: " + str(players["Computer"][0]) + ", computer's final score: " + str(players["Computer"][1]))
  print()


logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

##################################################



import random
#from replit import clear
#from art import logo
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def continue_decider(condition_1):
  if condition_1 == "y":
    return True
  elif condition_1 == "n":
    return False


play = True

if continue_decider(input("  Do you want to play a game of blackjack? Type 'y' or 'n': ")):
  play = True
  print()
else:
  play = False

while play:

 # clear()
 # print(logo)
  #Create the dictionary for the cards and scores
  players = {
    "Player": [[], 0],
    "Computer": [[], 0],
  }

  #First round cards
  for i in range(2):
    players["Player"][0].append(random.choice(cards))
    players["Computer"][0].append(random.choice(cards))

  count_scores(players)  
  print_scores()

  draw_one_card()
  
  evaluate()

  if continue_decider(input("  Do you want to play another game of blackjack? Type 'y' or 'n': ")):
    play = True
    print()
  else:
    play = False
