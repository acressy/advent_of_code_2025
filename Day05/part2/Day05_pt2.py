#! /usr/bin/env python3

with open("test_input.txt","r") as infile:
    ranges = []
    new_ranges = []
    for line in infile:
        if "-" in line:
            start=int(line.strip().split("-")[0])
            end=int(line.strip().split("-")[1])
            ranges.append([start,end])
    print(ranges)
    for i in range(0,len(ranges)):
        print(new_ranges)
        s = int(ranges[i][0])
        e = int(ranges[i][1])
        if i == 0:
            new_ranges.append(ranges[0])
        else:
            print(len(new_ranges))
            for n in range(0,len(new_ranges)):
                ns=int(new_ranges[n][0])
                ne=int(new_ranges[n][1])
                if s < ns and e > ns:
                    print(str(s) + " is less than " + str(ns) + " and " + str(e) + " is greater than " + str(ns))

                    if e > ne:
                        new_ranges[n] = [str(s),str(e)]
                        print(str(e) + " is greater than " + str(ne))
                    else:
                        new_ranges[n] = [str(s),str(ne)]
                elif s > ns and s<ne and e > ne:
                    print(str(s) + " is greater than " + str(ns) + " but less than " + str(ne) + " and " + str(e) +" is greater than " + str(ne))
                    new_ranges[n] = [str(ns),str(e)]
                elif s > ns and e < ne:
                    continue
                else:
                    new_ranges.append(ranges[i])
    print(new_ranges)


#         for n in range(my_range[0],my_range[1]+1):
#             if n not in fresh_list:
#                 fresh_list.append(str(n))

# fresh_count=len(fresh_list)

# with open("fresh_count.txt","w") as outfile:
#     outfile.write(str(fresh_count))

# Instead of listing everything out, we should really be seeing where the ranges have overlap and subtracting from there
# The current method is very time consuming and causes timeout errors

# if the start or end is within the range of other starts and ends, it should get combined with what it overlaps with

# Gotten out of the timeout errors but now the appending thing at the end is not working well.