# Part 1 for now because idk how to solve part 2 lmao
import sys
import re
#import functools
I = sys.stdin.read().splitlines()

def combine(intervals):
    while True:
        combined = False
        break_flag = False
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if i==j:
                    continue
                i_s,i_e = intervals[i]
                j_s,j_e = intervals[j]
                all_se = sorted([i_s,j_s,i_e,j_e])
                if all_se == [i_s,j_s,j_e,i_e]:
                    intervals.remove([i_s,i_e])
                    intervals.remove([j_s,j_e])
                    intervals += [[i_s,i_e]]
                    break_flag = True
                    combined = True
                    break
                elif all_se == [j_s,i_s,i_e,j_e]:
                    intervals.remove([i_s,i_e])
                    intervals.remove([j_s,j_e])
                    intervals += [[j_s,j_e]]
                    break_flag = True
                    combined = True
                    break
                elif all_se == [i_s, j_s, i_e, j_e]:
                    intervals.remove([i_s,i_e])
                    intervals.remove([j_s,j_e])
                    intervals += [[i_s,j_e]]
                    break_flag = True
                    combined = True
                    break
                elif all_se == [j_s,i_s,j_e,i_e]:
                    intervals.remove([i_s,i_e])
                    intervals.remove([j_s,j_e])
                    intervals += [[j_s,i_e]]
                    break_flag = True
                    combined = True
                    break
            if break_flag:
                break
        if not combined:
            return intervals

check_y = 2000000
intervals = []
beacons_x = set()
for i in I:
    x,y,b_x,b_y = map(int,re.findall(r"Sensor at x=([0-9\-]+), y=([0-9\-]+): closest beacon is at x=([0-9\-]+), y=([0-9\-]+)",i)[0])
    d = abs(x-b_x) + abs(y-b_y)
    y_d = abs(y-check_y)
    if b_y == check_y:
        beacons_x |= {b_x}
    if y_d <= d:
        interval = [x-d+y_d,x+d-y_d]
        intervals += [interval]

intervals = combine(intervals)
ans = 0
for s,e in intervals:
    for x in beacons_x:
        if s <= x <= e:
            ans -= 1
    ans += e-s+1
print(ans)
