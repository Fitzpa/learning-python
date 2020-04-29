"""Example using ranges in a for loop"""

# ranges go up to but not including the stop value

# When using a range with two arguments, the first argument is the starting index
# and the second argument - 1 is the last index.
for i in range(1, 21):
    print("i is now {}".format(i))
print('\n')  # newline

# When defining a range with only a single argument,
# the starting index defaults to zero and the single argument is the stop value.
for i in range(10):
    print("i is now {}".format(i))
print('\n')  # newline

# When defining a range with three arguments,
# the first is the starting index,
# the second is the stop value, and the third is step by amount.
for i in range(0, 10, 2):
    # this code will print out the numbers 0 through 9 by steps of 2.
    # 0, 2, 4, 6, 8
    print("i is now {}".format(i))
print('\n')  # newline

# When defining a range with three arguments,
# where the range steps down instead of up,
# the first is the starting index,
# the second is the stop value,
# and the third is step by amount as a negative number.
for i in range(10, 0, -2):
    # this code will print out the numbers 0 through 9 by steps of 2.
    # 0, 2, 4, 6, 8
    print("i is now {}".format(i))
