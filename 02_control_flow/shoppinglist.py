"""
Example of using a List in Python,
Which is an array in other languages like javaScript,
and then iterating through the List.
"""

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

# Here is another way to write the above code,
# utilizing continue
for item in shopping_list:
    if item == "spam":
        continue
    print("Buy " + item)
