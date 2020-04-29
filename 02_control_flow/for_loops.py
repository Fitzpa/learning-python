"""For Loop Examples"""


parrot = "Norwegian Blue"

for character in parrot:
    print(character)


num = "9,234;456:098,234.086"
separators = ""

for char in num:
    if not char.isnumeric():
        separators += char
print(separators)

values = "".join(
    char if char not in separators else " " for char in num).split()
print([int(val) for val in values])


# interactive version of the previous example
# where the final output will be the sum of all the groups of numbers
num = input("Please enter a series of numbers, using and separators you like: ")
separators = ""

for char in num:
    if not char.isnumeric():
        separators += char

values = "".join(
    char if char not in separators else " " for char in num).split()
print(sum([int(val) for val in values]))
