#! /usr/bin/env python3

# Define starts
position = 50
zero_count = 0

# Define functions
def move_the_dial(position, dir, num):
    # Move the dial
    if dir == "R":
        position = int(position) + int(num)
    elif dir == "L":
        position = int(position) - int(num)
    else:
        print("Invalid direction. Input can only be L### or R###.")
        exit
    return position
def normalize(position):
    while position > 99 or position < 0: # While loop to handle numbers greater than 100
            if position > 99:
                position = position - 100
            if position < 0:
                position = position + 100
    return position

# Loop through text & call functions
with open("input.txt", "r") as file:
    for line in file:
        dir=list(line)[0]
        num=int(line[1:])

        position = move_the_dial(position,dir,num)

        # Normalize the position (since the dial is circular)
        position = normalize(position)

        if position == 0:
            zero_count += 1

# Print password to open the door!
with open("password.txt", "w") as outfile:
    outfile.write(str(zero_count))
