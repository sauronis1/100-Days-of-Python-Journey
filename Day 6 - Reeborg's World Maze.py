#Reeborg's World - Maze Algorithm
#I will have to come back after day 15 to debug this! Only managed to debug it for test world 1.

def turn_right():
  turn_left()
  turn_left()
  turn_left()

while not at_goal():
  if right_is_clear() is True:
      turn_right()
      while front_is_clear() is True:
          move()
  elif wall_in_front() is True:
      turn_left()
  else:
      move()