low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")
guess = 1
while True:
    guess = low + (high - low) // 2
