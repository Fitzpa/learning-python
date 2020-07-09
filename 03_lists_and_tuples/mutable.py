shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 'bread',
                 "rice"
                 ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))

print()
a = b = c = d = another_list
print(a)
print("Adding Cream to shopping list")
b.append("Cream")
print(c)
