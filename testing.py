import sys
import re
I = sys.stdin.read().splitlines()
visited = [[0,0]]
H = [0,0]
T = [0,0]
for i in I:
    d,move = i.split()
    move = int(move)
    for _ in range(move):
        prev_H = H.copy()
        if d == "R":
            H[0] += 1
        if d == "L":
            H[0] -= 1
        if d == "U":
            H[1] += 1
        if d == "D":
            H[1] -= 1
        if not (abs(T[0] - H[0]) <= 1 and abs(T[1] - H[1]) <= 1):
            T = prev_H.copy()
            if T not in visited:
                visited += [T]
print(len(visited))

visited = [[0,0]]
chain = [[0,0] for i in range(10)]

def sign(a,b):
    if a>b:
        return 1
    if a==b:
        return 0
    return -1

def move_chain(chain,num):
    x_h,y_h = chain[num-1]
    x_t,y_t = chain[num]
    if not (abs(x_h-x_t) <= 1 and abs(y_h-y_t) <= 1):
        chain[num][0] += sign(x_h,x_t)
        chain[num][1] += sign(y_h,y_t)
    return chain

for i in I:
    d,move = i.split()
    move = int(move)
    for _ in range(move):
        if d == "R":
            chain[0][0] += 1
        if d == "L":
            chain[0][0] -= 1
        if d == "U":
            chain[0][1] += 1
        if d == "D":
            chain[0][1] -= 1
        for x in range(1,10):
            chain = move_chain(chain,x).copy()
        if chain[9] not in visited:
            visited += [chain[9].copy()]
print(len(visited))
