#1 - Logo
print('''
 __          ___    _       _______                                         
 \ \        / / |  | |   /\|__   __|                                        
  \ \  /\  / /| |__| |  /  \  | |                                           
   \ \/  \/ / |  __  | / /\ \ | |                                           
    \  /\  /  | |  | |/ ____ \| |                                           
  _  \/  \/   |_|  |_/_/    \_\_|                _                          
 (_)     | | | |                                | |                         
  _ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __            
 | / __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|           
 | \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |              
 |_|___/_ \__|_| |_|\___| |_| |_|\__,_|_| |_|_|_|_.__/ \___|_|      __ ___  
 |_   _( )           | | | |   (_)     | |  (_)                    / _|__ \ 
   | | |/ _ __ ___   | |_| |__  _ _ __ | | ___ _ __   __ _    ___ | |_   ) |
   | |   | '_ ` _ \  | __| '_ \| | '_ \| |/ / | '_ \ / _` |  / _ \|  _| / / 
  _| |_  | | | | | | | |_| | | | | | | |   <| | | | | (_| | | (_) | |  |_|  
 |_____| |_| |_| |_|  \__|_| |_|_|_| |_|_|\_\_|_| |_|\__, |  \___/|_|  (_)  
                                                      __/ |                 
                                                     |___/                  

''')
#2 - Make the computer choose a number between 1 and 100 (import random)
import random
THE_NUMBER = random.randint(1, 100)

def assign_difficulty():
  #3 Difficulty - easy or hard.
  difficulty = input("Choose whether you want to play on 'easy' or 'hard': ")
  #4 Assign lives based on difficulty
  if difficulty == "easy":
    lives = 10
  elif difficulty == "hard":
    lives = 5
  else:
    lives = 0
  return lives
  #5 Function that takes the user guess and evaluates it

def make_a_guess():
  global lives
  global guess_again
  print(f"You have {lives} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  print()

  if guess > THE_NUMBER:
    print("Too high.")
    lives -= 1
  elif guess < THE_NUMBER:
    print("Too low.")
    lives -= 1
  elif guess == THE_NUMBER:
    print(f"You got it! The answer was {THE_NUMBER}")
    guess_again = False
    return guess_again

  if lives == 0:
    print("You've run out of guesses. You lose.")
    guess_again = False
    return guess_again
  else:
    print("Guess again.")
############THE GAME################

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
lives = assign_difficulty()

guess_again = True
while guess_again:
  make_a_guess()
