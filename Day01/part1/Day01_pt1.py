#! /usr/bin/env python3

# Define starts
position = 50
zero_count = 0


with open("input.txt", "r") as file:
    for line in file:
        dir=list(line)[0]
        num=int(line[1:])

        # Move the dial
        if dir == "R":
            position = int(position) + int(num)
        elif dir == "L":
            position = int(position) - int(num)
        else:
            print("Invalid direction. Input can only be L### or R###.")
            exit

        # Normalize the position (since the dial is circular)
        while position > 99 or position < 0: # While loop to handle numbers greater than 100
            if position > 99:
                position = position - 100
            if position < 0:
                position = position + 100
            
        if position == 0:
            zero_count += 1

# Print password to open the door!
with open("password.txt", "w") as outfile:
    outfile.write(str(zero_count))

