#! /usr/bin/env python3

with open("input.txt","r") as elevators:
    total_joltage = 0
    for bank in elevators:

        bank = bank.strip("\n")
        num_batteries = len(bank)
        batteries = list(bank)
        max_joltage = 0

        for i in range(0,num_batteries-1):
            first_digit = batteries[i]
            max_second = 0

            for j in range(i+1,num_batteries):
                number=int(str(first_digit)+str(batteries[j]))
                if number > max_joltage:
                    max_joltage=number

        # Add to the total joltage
        total_joltage += max_joltage

with open("total_joltage.txt", "w") as outfile:
    outfile.write(str(total_joltage))
                
                
