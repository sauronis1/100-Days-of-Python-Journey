#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

letters_ind = []
numbers_ind = []
symbols_ind = []

pass_letters = []
pass_symbols = []
pass_numbers = []

unscrambled = []

for i in range(0, nr_letters):
  letters_ind.append(random.randint(0,len(letters)-1))
for j in range (0, len(letters_ind)):
  pass_letters.append(letters[letters_ind[j]])
  unscrambled.append(pass_letters[j])

for i in range(0, nr_symbols):
  symbols_ind.append(random.randint(0,len(symbols)-1))
for l in range (0, len(symbols_ind)):
  pass_symbols.append(symbols[symbols_ind[l]])
  unscrambled.append(pass_symbols[l])

for i in range(0, nr_numbers):
  numbers_ind.append(random.randint(0,len(numbers)-1))
for k in range (0, len(numbers_ind)):
  pass_numbers.append(numbers[numbers_ind[k]])
  unscrambled.append(pass_numbers[k])

password_unscrambled = ""
for i in range (0,len(unscrambled)):
  password_unscrambled += unscrambled[i]
  
print(f"Your unscrambled password is {password_unscrambled}")

#print(len(letters))
#print(letters_ind)
#print(symbols_ind)
#print(numbers_ind)
#print(pass_letters)
#print(pass_symbols)
#print(pass_numbers)
#print(password_unscrambled)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# scrambled_ind = []
# scrambled = []
# for i in range (0, len(unscrambled)):
#   scrambled_ind.append(random.randint(0, (len(unscrambled)-1)))
# for i in range(0, len(scrambled_ind)):
#   print(unscrambled[i])
#   print(scrambled_ind[i])
#   scrambled.append(unscrambled[scrambled_ind[i]])

# print(scrambled)
# password_scrambled = ""
# for i in range (0, len(scrambled)):
#   password_scrambled += scrambled[i]

random.shuffle(unscrambled)
password_scrambled = ""
for i in range(0, len(unscrambled)):
  password_scrambled += unscrambled[i]


#print(scrambled_ind)
print(f"Your scrambled password is {password_scrambled}")
