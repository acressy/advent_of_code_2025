#! /usr/bin/env python3

# Input the total number of batteries to use here:
max_batteries=12

with open("input.txt","r") as elevators:
    total_joltage = 0
    elevator_num = 0
    for bank in elevators:

        bank = bank.strip("\n")
        num_batteries = len(bank)
        batteries = list(bank)
        starting_index=0
        number = list("0"*max_batteries)

        for i in range(0,max_batteries):
            max_value=0
            for j in range(starting_index,num_batteries-(max_batteries-1)+i):
                if int(batteries[j]) > max_value:
                    max_value = int(batteries[j])
                    starting_index=j+1
            number[i] = str(max_value)
        total_joltage += int("".join(number))

with open("total_joltage.txt", "w") as outfile:
    outfile.write(str(total_joltage))
                
                
