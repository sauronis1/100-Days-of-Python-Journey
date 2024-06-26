""" #this method isn't optional because you can forget to close the file
file = open("text_file.txt")
contents = file.read()

print(contents)
file.close()
"""

with open("text_file.txt") as file:
    contents = file.read()
    print(contents)

with open("text_file.txt", mode="a") as f:
    f.write("\nHI!!!")
