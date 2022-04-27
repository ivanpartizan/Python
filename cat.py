def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            # return n
            break
    return n


def meow(n):
    for _ in range(n):
        print('meow')


# # # # # # # # # #
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

# for i in range(10):
#     print('meow')

# for i in [0, 1, 2]:
#     print('meow')

# print('meow\n' * 3, end='')

# i = 3
# while i != 0:
#     print('meow')
#     i = i - 1

# i = 0
# while i < 3:
#     print('meow')
#     i += 1
