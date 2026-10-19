#! /usr/bin/env python3

with open("input.txt","r") as infile:
    ranges = []
    ids = []
    fresh_list = []
    for line in infile:
        if "-" in line:
            start=int(line.strip().split("-")[0])
            end=int(line.strip().split("-")[1])
            ranges.append([start,end])
        elif line.strip() == "":
            continue
        else:
            ids.append(line.strip())
    for id in ids:
        for my_range in ranges:
            if int(id) in range(my_range[0],my_range[1]+1):
                if id not in fresh_list:
                    fresh_list.append(id)

with open("fresh_count.txt","w") as outfile:
    outfile.write(str(len(fresh_list)))


        