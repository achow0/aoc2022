import sys
import re
I = sys.stdin.read().splitlines()

c=0
s=1
ans=0
for i in I:
    i = i.split()
    if i[0] == "noop":
        c+=1
        if (c-20)%40 == 0:
            ans += c*s
    else:
        for _ in range(2):
            c+=1
            if (c-20)%40 == 0:
                ans += c*s
        s += int(i[1])
print(ans)


c=0
s=1
grid = [[None for i in range(40)]for a in range(6)]
for i in I:
    i = i.split()
    if i[0] == "noop":
        if c%40 in [s-1,s,s+1]:
            grid[c//40][c%40] = '#'
        else:
            grid[c//40][c%40] = ' '
        c+=1
    else:
        for _ in range(2):
            if c%40 in [s-1,s,s+1]:
                grid[c//40][c%40] = '#'
            else:
                grid[c//40][c%40] = ' '
            c+=1
        s += int(i[1])
print("\n".join(["".join(e) for e in grid]))
