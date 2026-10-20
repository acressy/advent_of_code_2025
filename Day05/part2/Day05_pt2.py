#! /usr/bin/env python3

counter = 0
with open("input.txt","r") as infile:
    ranges = []
    for line in infile:
        if "-" in line:
            start=int(line.strip().split("-")[0])
            end=int(line.strip().split("-")[1])
            ranges.append([start,end])

    # Check where there is overlap
    for i in range(0,2): # Loop through it twice to catch the overlaps
        for idx in range(0,len(ranges)):
            for sub_idx in range(0,len(ranges)):
                if idx != sub_idx:
                    if ranges[idx][0] <= ranges[sub_idx][0] and ranges[idx][1] >= ranges[sub_idx][0] and ranges[idx][1] <= ranges[sub_idx][1]:
                        ranges[idx]=[ranges[idx][0],ranges[sub_idx][1]]
                    elif ranges[idx][1] >= ranges[sub_idx][1] and ranges[idx][0] >= ranges[sub_idx][0] and ranges[idx][0] <= ranges[sub_idx][1]:
                        ranges[idx]=[ranges[sub_idx][0],ranges[idx][1]]
                    elif ranges[idx][1] <= ranges[sub_idx][1] and ranges[idx][0] >= ranges[sub_idx][0]:
                        ranges[idx]=[ranges[sub_idx][0],ranges[sub_idx][1]]
    
    # Only count the unique ranges
    unique_list = []
    for sublist in ranges:
        if sublist not in unique_list:
            unique_list.append(sublist)

    # Count the fresh items
    for item in unique_list:
        start = item[0]
        end = item[1]
        counter+=(end-start+1)

# Export the number of fresh IDs in the database!
with open("fresh_count.txt","w") as outfile:
    outfile.write(str(counter))