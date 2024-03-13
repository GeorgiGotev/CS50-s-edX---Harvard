# for _ in range(3):
#     print("#")

def main():
    print_colum(3)
    print_row(4)
    print_square(3)


def print_colum(height):
    # for _ in range(height):
    #     print("#")

    print("#\n" * height, end="")


def print_row(width):
    print("?" * width)


def print_square(size):
    for i in range(size):
        # for j in range(size):
        #     print("#", end="")

        # print()
        print("#" * size)


main()

