#! /usr/bin/env python3


def find_factors(n):
    factors=[]
    for i in range(1,n+1):
        if n % i == 0:
            factors.append(i)
    return factors


invalid_list=[]
with open("input.txt", "r") as file:
    for line in file:
        items=line.split(",")
        
        # Divide into ranges
        for item in items:
            start=int(item.split("-")[0])
            end=int(item.split("-")[1])

            # Call each possible number in the range
            for i in range(start,end+1):
                i = str(i)

                # What are the different ways we can split up each number?
                factors = find_factors(len(i))

                # Work through each possible factor (except the last one)
                for j in range(len(factors)-1):
                    number_of_iterations=len(i)//int(factors[j])

                    # Handle the single digit repeats
                    if factors[j] == 1:
                        if i[0]*number_of_iterations == i:
                            invalid_list.append(int(i))

                    # Handle the other types of repeats
                    else:
                        if i[0:factors[j]]*number_of_iterations == i:
                            invalid_list.append(int(i))

# Add up the unique values
total=sum(set(invalid_list))

# Write the total of all the invalid IDs
with open("invalid_totals.txt", "w") as outfile:
    outfile.write(str(total))