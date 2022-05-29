# Indoor Voice
string = input("Enter some random text: ")
print(string.lower())

# Playback Speed
string = input("Enter some random text: ")
print(string.replace(" ", "..."))

# Making Faces


def convert(str):
    if ":)" in str:
        str = str.replace(":)", "🙂")
    if ":(" in str:
        str = str.replace(":(", "🙁")
    return str


def main():
    string = input("Enter some random text: ")
    output = convert(string)
    print(output)


main()

# Einstein
m = int(input("Enter mass in kilograms: "))
c = 300000000
E = m * pow(c, 2)
print(E)

# Tip Calculator


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(
        input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d.replace("$", ""))


def percent_to_float(p):
    return float(p.replace("%", "")) / 100


main()
