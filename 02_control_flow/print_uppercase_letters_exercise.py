"""Write a program that takes in a string and prints only
the uppercase letters using a for loop and an if statement"""

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
uppercase_letters = ""
for char in quote:
    if str(char).isupper():
        uppercase_letters += char

print(uppercase_letters)
