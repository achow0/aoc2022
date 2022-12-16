import sys
import re
#import functools
I1 = sys.stdin.read().splitlines()
I2 = I1.copy()

class Sensor:
    def __init__(self,x,y,b_x,b_y):
        self.x = x
        self.y = y
        self.b_x = b_x
        self.b_y = b_y
        self.d = abs(self.x-self.b_x) + abs(self.y-self.b_y)

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
                elif all_se == [i_s,i_e,j_s,j_e] and i_e == j_s-1:
                    intervals.remove([i_s,i_e])
                    intervals.remove([j_s,j_e])
                    intervals += [[i_s,j_e]]
                    break_flag = True
                    combined = True
                    break
                elif all_se == [j_s,j_e,i_s,i_e] and j_e == i_s-1:
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
b_check_y = set()
sensors = []
for i in I1:
    x,y,b_x,b_y = map(int,re.findall(r"Sensor at x=([0-9\-]+), y=([0-9\-]+): closest beacon is at x=([0-9\-]+), y=([0-9\-]+)",i)[0])
    sensors += [Sensor(x,y,b_x,b_y)]
    if b_y == check_y:
        b_check_y |= {b_x}
b_check_y = len(b_check_y)

max_val = 4000000

for Y in range(max_val+1):
    intervals = []
    for s in sensors:
        y_d = abs(s.y-Y)
        if y_d <= s.d:
            intervals += [[s.x-s.d+y_d,s.x+s.d-y_d]]
    intervals = [[s,e] for s,e in sorted(combine(intervals)) if s<=max_val]
    if Y == check_y:
        ans = 0
        for s,e in intervals:
            ans += e-s+1
        print(ans-b_check_y)
    if len(intervals) == 2:
        X = intervals[0][1] + 1
        print(Y + 4000000 * X)
        break
