#!/bin/python3

# Define starts
position = 50
zero_count = 0

# Loop through text & call functions
with open("input.txt", "r") as file:
    for line in file:
        dir=list(line)[0]
        num=int(line[1:])

        for i in range(num):
            # Handle the turn directions
            if dir == "R":
                position += 1
            if dir == "L":
                position -= 1

            # Handle when numbers pass the dial range
            if position > 99:
                position -= 100
            if position < 0:
                position += 100

            # Count when we pass/land on 0
            if position == 0:
                zero_count += 1

# Print password to open the door!
with open("password.txt", "w") as outfile:
    outfile.write(str(zero_count))
