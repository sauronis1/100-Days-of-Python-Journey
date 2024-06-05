import game_data
data_local = game_data.data
import art
import random
from replit import clear

compare_A = random.choice(data_local)
compare_B = {}
current_score = 0

game_not_over = True
round = 0

while game_not_over:
  data_local.remove(compare_A)
  print(art.logo)
  if round > 0:
    print(f"You're right! Current score: {current_score}")

  print(f"Compare A: {compare_A['name']}, a {compare_A['description']}, from {compare_A['country']}.")
  print(art.vs)

  compare_B = random.choice(data_local)
  print(f"Against B: {compare_B['name']}, a {compare_B['description']}, from {compare_B['country']}.")

  user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  if user_guess == 'a' and compare_A["follower_count"] > compare_B["follower_count"]:
    current_score += 1
    round += 1
  elif user_guess == 'b' and compare_B["follower_count"] > compare_A["follower_count"]:
    current_score += 1
    round += 1
  else:
    game_not_over = False

  clear()
  compare_A = compare_B

print(art.logo)
print(f"Sorry, that's wrong. Final score: {current_score}")
