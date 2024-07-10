"""

# FileNotFound

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["ffffffssssff"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is an error that I made up.")
    file.close()
    print("File was closed.")

# KeyError
#a_dictionary = {"key": "value"}
#value = a_dictionary["key that doesn't exist"]

"""

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height is not over 3 meters.")

bmi = weight / height ** 2
print(bmi)