import sys
import re
I = sys.stdin.read().splitlines()
I = [[*map(int,i)] for i in I]

def check_visible(I,x,y):
    if x==0 or y==0 or x==len(I)-1 or y==len(I[0])-1:
        return 1
    else:
        if max(I[x][:y]) < I[x][y]:
            return 1
        if max(I[x][y+1:]) < I[x][y]:
            return 1
        if max([I[i][y] for i in range(x)]) < I[x][y]:
            return 1
        if max(I[i][y] for i in range(x+1,len(I))) < I[x][y]:
            return 1
        return 0

def scenic_score(I,x,y):
    if x==0 or y==0 or x==len(I)-1 or y==len(I[0])-1:
        return 0
    else:
        s = 1
        for i in range(1,y+1):
            if I[x][y-i] >= I[x][y]:
                break
        s *= i
        for i in range(1,len(I[0]) - y):
            if I[x][y+i] >= I[x][y]:
                break
        s *= i
        for i in range(1,x+1):
            if I[x-i][y] >= I[x][y]:
                break
        s *= i
        for i in range(1,len(I) - x):
            if I[x+i][y] >= I[x][y]:
                break
        s *= i
        return s

v = 0
max_s = 0
for a in range(len(I)):
    for b in range(len(I[0])):
        if check_visible(I,a,b):
            v += 1
            max_s = max(max_s,scenic_score(I,a,b))
print(v,max_s)
