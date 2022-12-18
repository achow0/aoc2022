import sys
import re
#import functools
I = sys.stdin.read().strip()#.splitlines()
len_I = len(I)
shapes = [[0,1,2,3],
          [1,1j,1+1j,1+2j,2+1j],
          [0,1,2,2+1j,2+2j],
          [0,1j,2j,3j],
          [0,1j,1,1+1j]]

rocks = {*range(7)}
max_height = 0

read_index = 0

for i in range(2022):
    shape = shapes[i%5]
    loc = complex(2,max_height+4)
    shape_pos = tuple(pos + loc for pos in shape)
    while True:
        d = I[read_index]
        right = tuple(pos + 1 for pos in shape_pos)
        rightmost = max(right,key = lambda x:x.real)
        left = tuple(pos - 1 for pos in shape_pos)
        leftmost = min(left,key = lambda x:x.real)
        if d == ">" and all(pos not in rocks for pos in right) and rightmost.real < 7:
            shape_pos = right
        elif d == "<" and all(pos not in rocks for pos in left) and leftmost.real > -1:
            shape_pos = left
        read_index += 1
        read_index %= len_I
        break_flag = False
        for loc in shape_pos:
            if loc - 1j in rocks:
                rocks |= {*shape_pos}
                break_flag = True
                break
        if break_flag:
            break
        shape_pos = tuple(pos - 1j for pos in shape_pos)
    max_height = max(max_height,max(pos.imag for pos in shape_pos))
print(max_height)
