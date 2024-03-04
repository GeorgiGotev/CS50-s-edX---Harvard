name = input ("What's your name?").title().strip()


# trim/capitalize and more our input
# name = name.strip()
# name = name.capitalize()
# name = name.title()

# print(f"Hello, {name.title().strip()}!")

# split
first, last = name.split(" ")

print(f"Hello, {first} {last}!")
