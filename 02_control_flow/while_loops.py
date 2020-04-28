"""Examples of how to use while loops"""

# While loops
count = 0
while count <= 100:
    print('The current count is ' + str(count) + '.')
    count += 1

name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you')

name = ''
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break  # you can use a break statement to exit an infinite loop
print('Thanks for doing that!')

count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    # when the continue function is called, the executing
    # immediately jumps back to the start of the code.
    # So here it would never print 'count is 3'
    print('count is ' + str(count))
