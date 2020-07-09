"""
Working with Lists.
Using append method on a List.
Iterating over a List.
"""
available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse pad",
                   "hdmi cable"
                   ]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = []  # create an empty list

while current_choice != "0":
    if current_choice in valid_choices:
        print("Adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)

    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))
        print("0: To Finish")

    current_choice = input()
print()
print("Current list of computer parts: {}".format(computer_parts))
