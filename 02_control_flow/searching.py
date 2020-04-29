"""An example of how to use the break function when searching for a item in a List"""

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "milk"
found_at = None

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is None:
    print("The item {} was not found in the List".format(item_to_find))
else:
    print("{0} was found at index {1}.".format(item_to_find, found_at))
