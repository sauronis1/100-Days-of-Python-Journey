#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt") as names_data:
    names_list = names_data.readlines()

for name in names_list:
    fixed_name = name.strip("\n")
    with open("./Input/Letters/starting_letter.txt") as letter:
        letter_content = letter.read()
        new_content = letter_content.replace("[name]", fixed_name)
        letter_with_name = open(f"./Output/ReadyToSend/letter_for_{fixed_name}.txt", "x")
        letter_with_name.write(new_content)

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

"""
with open("./Input/Names/invited_names.txt") as names_data:
    names_list = names_data.readlines()

for name in names_list:
    fixed_name = name.strip("\n")
    with open("./Input/Letters/starting_letter.txt") as letter:
        letter_content = letter.readlines()
        print(letter_content)
        first_line = letter_content[0].replace("[name]", fixed_name)
        letter_with_name = open(f"./Output/ReadyToSend/{fixed_name}.txt", "x")
        letter_with_name.write(first_line)
        for line in letter_content[1:]:
            letter_with_name.write(line)
"""