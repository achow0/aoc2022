import sys
import re
I = sys.stdin.read().splitlines()

grid = []
visited = []
s_x = None
s_y = None
e_x = None
e_y = None

for x,i in enumerate(I):
    temp = []
    temp2 = []
    for y,e in enumerate(i):
        if e == "S":
            temp += [ord("a")]
            s_x = x
            s_y = y
        elif e == "E":
            temp += [ord("z")]
            e_x = x
            e_y = y
        else:
            temp += [ord(e)]
        temp2 += [0]
    grid += [temp.copy()]
    visited += [temp2.copy()]

Q = []
parents = {}
visited[s_x][s_y] = 1
Q.append([s_x,s_y])
while Q:
    v = Q.pop(0)
    v_x = v[0]
    v_y = v[1]
    if v == [e_x,e_y]:
        break
    possible_dir = [d for d in [[1,0],[0,1],[-1,0],[0,-1]] if -1 < v_x+d[0] < len(grid) and -1 < v_y+d[1] < len(grid[0])]
    for x_dir,y_dir in possible_dir:
        w_x = v_x + x_dir
        w_y = v_y + y_dir
        if not visited[w_x][w_y] and grid[w_x][w_y]-grid[v_x][v_y] < 2:
            visited[w_x][w_y] = 1
            Q.append([w_x,w_y])
            parents[(w_x,w_y)] = (v_x,v_y)

coords = (e_x,e_y)
distance = 1
while parents[coords] != (s_x,s_y):
    coords = parents[coords]
    distance += 1

print(distance)

all_a = []
for x,row in enumerate(grid):
    for y,e in enumerate(row):
        if e == ord("a"):
            all_a += [[x,y]]

min_length = 10000
for s_x,s_y in all_a:
    visited = [[0 for y in range(len(grid[0]))] for x in range(len(grid))]
    Q = []
    parents = {}
    visited[s_x][s_y] = 1
    Q.append([s_x,s_y])
    while Q:
        v = Q.pop(0)
        v_x = v[0]
        v_y = v[1]
        if v == [e_x,e_y]:
            break
        possible_dir = [d for d in [[1,0],[0,1],[-1,0],[0,-1]] if -1 < v_x+d[0] < len(grid) and -1 < v_y+d[1] < len(grid[0])]
        for x_dir,y_dir in possible_dir:
            w_x = v_x + x_dir
            w_y = v_y + y_dir
            if not visited[w_x][w_y] and grid[w_x][w_y]-grid[v_x][v_y] < 2:
                visited[w_x][w_y] = 1
                Q.append([w_x,w_y])
                parents[(w_x,w_y)] = (v_x,v_y)

    coords = (e_x,e_y)
    distance = 1
    if coords in parents:
        while parents[coords] != (s_x,s_y):
            coords = parents[coords]
            distance += 1

        if distance < min_length:
            min_length = distance
print(min_length)
