def main():
    print_square(3)
    # print_row(4)
    # print_column(3)


def print_square(size):
    # For each row in square
    for i in range(size):
      # For each brick in row
        for j in range(size):
            # Print brick
            print("#", end="")

        print()


# New version


def print_square(size):
    for i in range(size):
        print("#" * size)


def print_row(width):
    print("?" * width)


def print_column(height):
    print("#\n" * height, end="")
    # for _ in range(height):
    #     print("#")

# for _ in range(3):
#     print('#')


main()
