#! /usr/bin/env python3

# Define function to count items (like '@','x', and '.')
def count_item(df1,item):
    count = 0
    for i in range(0,len(df1)):
        for j in range(0,len(df1[0])):
            if df1[i][j] == item:
                count += 1
    return count

# Define function to assign removable rolls
def assign_removables(my_df):
    for i in range(0,len(my_df)):
        for j in range(0,len(my_df[i])):
            if my_df[i][j] == "@":
                adjacent_rolls=0
                # Count adjacent paper rolls
                for m in range(i-1,i+2):
                    for n in range(j-1,j+2):
                        if m < 0:
                            continue
                        if m >= len(my_df):
                            continue
                        if n < 0:
                            continue
                        if n >= len(my_df[0]):
                            continue
                        if m == i and n == j:
                            continue
                        if my_df[m][n] == "@" or my_df[m][n] == "x" :
                            adjacent_rolls += 1

                if adjacent_rolls < 4:
                    my_df[i][j] = "x"
    return my_df

# Define function to remove the removable rolls
def remove_rolls(df2):
    for i in range(0,len(df2)):
        for j in range(0,len(df2[0])):
            if df2[i][j] == "x":
                df2[i][j] = "."
    return df2

# Read and loop through the input file
with open("input.txt","r") as file:

    # Make df (not using packages like pandas)
    dept_floor=[]
    for line in file:
        dept_floor.append(list(line.strip()))
    num_spaces=(len(dept_floor)*len(dept_floor[0]))

    # Define what is initially removable
    new_df = assign_removables(dept_floor)
    num_x = count_item(new_df,"x")
    removable_count = num_x

    # Loop until we cant remove anymore
    while num_x > 0:
        new_df = remove_rolls(new_df)
        new_df = assign_removables(new_df)
        num_x = count_item(new_df,"x")
        removable_count += num_x

# Write how many paper rolls we can remove from the printing room!
with open("removable_rolls.txt","w") as outfile:
    outfile.write(str(removable_count))
