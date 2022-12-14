import sys
#import re
#import functools
I = sys.stdin.read().splitlines()
depth_dict = {i:set() for i in range(200)}
max_depth = 0
for l in I:
    l = l.split(" -> ")
    for i in range(len(l)-1):
        x1,d1 = map(int,l[i].split(","))
        x2,d2 = map(int,l[i+1].split(","))
        if d1 not in depth_dict:
            depth_dict[d1] = set()
        if d2 not in depth_dict:
            depth_dict[d2] = set()
        if d1 > max_depth:
            max_depth = d1
        if d2 > max_depth:
            max_depth = d2
        if d1 == d2:
            x1,x2 = sorted([x1,x2])
            depth_dict[d1] |= {*range(x1,x2+1)}
        else:
            d1,d2 = sorted([d1,d2])
            for d in range(d1,d2+1):
                if d not in depth_dict:
                    depth_dict[d] = {x1}
                else:
                    depth_dict[d] |= {x1}
sand = 0
curr_sand = ()
settled = True
pt1_flag = False

while True:
    if settled:
        curr_sand = (500,0)
        settled = False
    else:
        if curr_sand[1] + 1 == max_depth + 2:
            sand += 1
            depth_dict[curr_sand[1]] |= {curr_sand[0]}
            settled = True
            continue
        down = (curr_sand[0],curr_sand[1] + 1)
        left = (curr_sand[0]-1,curr_sand[1] + 1)
        right = (curr_sand[0]+1,curr_sand[1] + 1)
        if down[0] not in depth_dict[down[1]]:
            curr_sand = down
        elif left[0] not in depth_dict[left[1]]:
            curr_sand = left
        elif right[0] not in depth_dict[right[1]]:
            curr_sand = right
        else:
            sand += 1
            depth_dict[curr_sand[1]] |= {curr_sand[0]}
            settled = True
    if not pt1_flag and curr_sand[1] > max_depth:
        print(sand)
        pt1_flag = True
    if 499 in depth_dict[1] and 500 in depth_dict[1] and 501 in depth_dict[1]:
        break
print(sand+1)
