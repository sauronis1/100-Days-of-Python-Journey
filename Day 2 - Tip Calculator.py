#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = float(input("Celkový účet v Kč?  "))
tip = int(input("Kolik chceš nechat dýško v procentech?  "))
people = int(input("Kolik lidí si to rozdělí?  "))

total_bill = bill+((bill/100)*tip)
rozděleno = total_bill/people
zaokrouhleno = round(rozděleno, 2)
print(f"Každý zaplatí {zaokrouhleno}Kč")