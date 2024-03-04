# ask user for their name...
name = input("What is your name? ")

# say hello to user.
print(f"Hello, {name}!")
print("Hello, " + name + "!")


print("Hello,",name+"!")
# change the separator in the basic print
print("Hello,", name, sep="...")

# combine two lines and print them inline
print("Hello, ", end="")
print(name + "!")
print('Hello, "friend"!')
print("Hello, \"friend\"!")