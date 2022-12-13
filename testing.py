import sys
import re
import functools
I = sys.stdin.read()
I_1 = I.split("\n\n")
s = 0

def compare(l,r):
    if type(l) == int and type(r) == int:
        if l == r:
            return "same"
        return int(l < r)
    elif type(l) == list and type(r) == int:
        return compare(l,[r])
    elif type(l) == int and type(r) == list:
        return compare([l],r)
    else:
        for a, b in zip(l,r):
            result = compare(a,b)
            if result != "same":
                return result
        if len(l) > len(r):
            return 0
        elif len(r) > len(l):
            return 1
        return "same"

for i,a in enumerate(I_1):
    l,r = map(eval,a.strip().split("\n"))
    if compare(l,r):
        s += i+1
print(s)

I_2 = I.splitlines()
arr = [eval(i.strip()) for i in [e for e in I_2 if e!=""]] + [[[2]],[[6]]]
arr.sort(key = functools.cmp_to_key(lambda l,r: -1 if compare(l,r) else 1))
print((arr.index([[2]])+1)*(arr.index([[6]])+1))
