#! /usr/bin/env python3

with open("input.txt","r") as file:
    dept_floor=[]
    for line in file:
        dept_floor.append(list(line.strip()))
    accessible_by_forklift=0
    for i in range(0,len(dept_floor)):
        for j in range(0,len(dept_floor[i])):
            if dept_floor[i][j] == "@":
                adjacent_rolls=0
                # Count adjacent paper rolls
                for m in range(i-1,i+2):
                    for n in range(j-1,j+2):
                        if m < 0:
                            continue
                        if m >= len(dept_floor):
                            continue
                        if n < 0:
                            continue
                        if n >= len(dept_floor[0]):
                            continue
                        if m == i and n == j:
                            continue
                        if dept_floor[m][n] == "@" or dept_floor[m][n] == "x" :
                            adjacent_rolls += 1

                if adjacent_rolls < 4:
                    dept_floor[i][j] = "x"
    for i in range(0,len(dept_floor)):
        for j in range(0,len(dept_floor[i])):
            if dept_floor[i][j] == "x":
                accessible_by_forklift+=1

with open("accessible_rolls.txt","w") as outfile:
    outfile.write(str(accessible_by_forklift))
