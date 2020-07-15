""" Common Sequence Operations """

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

print(min(even))
print(max(even))
print(min(odd))
print(max(odd))

print()
print(len(even))
print(len(odd))

print()
print("Mississippi".count("i"))

even.extend(odd)
print('even ', even)
print()
even.sort()
print('even sorted ascending', even)
even.sort(reverse=True)
print('even sorted descending', even)
# Lists are mutable
# The sort() method doesn't create a copy of the list. It just rearranges the order of the list in place.
