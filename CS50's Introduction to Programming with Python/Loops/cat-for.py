# for i in [0, 1, 2]:
#     print("Meow")


# for _ in range(3):
#     print("Meow")

# print("Meow\n" * 3, end="")


# while True:
#     n = int(input("What's n: "))
#     # if n < 0:
#     #     continue
#     # else:
#     #     break
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")
        

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n: "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")


main()