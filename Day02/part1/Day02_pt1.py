#! /usr/bin/env python3

invalid_total = 0
with open("input.txt", "r") as file:
    for line in file:
        items=line.split(",")
        for item in items:
            start=int(item.split("-")[0])
            end=int(item.split("-")[1])
            for i in range(start,end+1):
                i = str(i)
                if len(i) % 2 == 0:
                    if i[0:(len(i)//2)]==i[(len(i)//2):len(i)]:
                        invalid_total+=int(i)

with open("invalid_totals.txt", "w") as outfile:
    outfile.write(str(invalid_total))