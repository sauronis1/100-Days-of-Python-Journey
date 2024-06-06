from game_data import data
from art import logo
from art import vs
import random
from replit import clear



def the_account_information(account):
  account_name = account["name"]
  account_description = account["description"]
  account_country = account["country"]

  account_information = f"{account_name}, a {account_description}, from {account_country}"
  return account_information

def assign_random_account():
  account = random.choice(data)
  return account

def check_if_guess_correct(account_A, account_B):
  guess = input("Which one has more followers? Type 'A' or 'B': ").lower()
  if account_A["follower_count"] > account_B["follower_count"]:
    return guess == "a"
  else:
    return guess == 'b'

def should_play_again():
  question = input("Would you like the play the game again? Type 'Y' or 'N': ").lower()
  if question == 'n':
    return False
  else:
    return True



def game():

  play_again = True

  while play_again:

    keep_going = True
    score = 0
    account_A = assign_random_account()
    account_B = assign_random_account()
    print(logo)
    while keep_going:
      account_A = account_B
      account_B = assign_random_account()

      while account_A == account_B:
        account_B = assign_random_account()

      print(f"Compare A: {the_account_information(account_A)}")
      print(vs)
      print(f"Against B: {the_account_information(account_B)}")

      user_guess = check_if_guess_correct(account_A, account_B)

      clear()
      print(logo)

      if user_guess:
        score += 1
        print(f"You're right! Your current score is: {score}")
      else:
        keep_going = False
        print(f"Sorry, that was wrong. Your final score is: {score}")


    play_again = should_play_again()
    clear()


game()