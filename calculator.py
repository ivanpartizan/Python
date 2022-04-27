def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    # return n * n
    # return n ** 2
    return pow(n, 2)


main()

# x = int(input("What's x? "))
# y = int(input("What's y? "))

# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = round(x + y)
# z = round(x / y, 2)
# z = x / y

# print(f"{z:,}")
# print(z)
# print(f"{z:.2f}")
