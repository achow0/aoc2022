import sys
#import re
import functools
I = sys.stdin.read().strip().splitlines()
open_faces = {}
min_x = 100
min_y = 100
min_z = 100
max_x = 0
max_y = 0
max_z = 0

for i in I:
    curr = tuple(map(int,i.split(",")))
    if curr[0] < min_x:
        min_x = curr[0]
    if curr[0] > max_x:
        max_x = curr[0]
    if curr[1] < min_y:
        min_y = curr[1]
    if curr[1] > max_y:
        max_y = curr[1]
    if curr[2] < min_z:
        min_z = curr[2]
    if curr[2] > max_z:
        max_z = curr[2]
    if curr not in open_faces:
        open_faces[curr] = 6
cubes = {*open_faces.keys()}

for curr in open_faces:
    if (curr[0],curr[1],curr[2]-1) in open_faces:
        open_faces[curr] -= 1
    if (curr[0],curr[1],curr[2]+1) in open_faces:
        open_faces[curr] -= 1
    if (curr[0],curr[1]-1,curr[2]) in open_faces:
        open_faces[curr] -= 1
    if (curr[0],curr[1]+1,curr[2]) in open_faces:
        open_faces[curr] -= 1
    if (curr[0]+1,curr[1],curr[2]) in open_faces:
        open_faces[curr] -= 1
    if (curr[0]-1,curr[1],curr[2]) in open_faces:
        open_faces[curr] -= 1

ans = sum(open_faces.values())
print(ans)

trapped = set()
non_trapped = set()

for x in range(min_x,max_x+1):
    for y in range(min_y,max_y+1):
        for z in range(min_z,max_z+1):
            cube = (x,y,z)
            if cube in cubes or cube in trapped or cube in non_trapped:
                continue
            Q = [cube]
            visited = {cube}
            out = False
            while Q:
                v = Q.pop(0)
                vx,vy,vz = v
                if vx < min_x or vx > max_x or vy < min_y or vy > max_y or vz < min_z or vz > max_z:
                    out = True
                    break
                adjacent_list = ((vx+1,vy,vz),(vx-1,vy,vz),(vx,vy-1,vz),(vx,vy+1,vz),(vx,vy,vz-1),(vx,vy,vz+1))
                for adjacent in adjacent_list:
                    if adjacent in cubes:
                        continue
                    elif adjacent not in visited:
                        visited |= {adjacent}
                        Q += [adjacent]
            if out:
                non_trapped |= visited
            else:
                trapped |= visited

for cube in trapped:
    X,Y,Z = cube
    if (X,Y,Z-1) in open_faces:
        ans -= 1
    if (X,Y,Z+1) in open_faces:
        ans -= 1
    if (X,Y-1,Z) in open_faces:
        ans -= 1
    if (X,Y+1,Z) in open_faces:
        ans -= 1
    if (X+1,Y,Z) in open_faces:
        ans -= 1
    if (X-1,Y,Z) in open_faces:
        ans -= 1
print(ans)
