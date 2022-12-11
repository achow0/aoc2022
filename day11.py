import sys
import re
#I = sys.stdin.read().splitlines()

class M():
    def __init__(self,start,op,test):
        self.items = start
        self.op = op
        self.test = test

md = [M([99, 67, 92, 61, 83, 64, 98],lambda x:x*17,lambda x:4 if x%3==0 else 2),
      M([78, 74, 88, 89, 50],lambda x:x*11,lambda x:3 if x%5==0 else 5),
      M([98,91],lambda x:x+4,lambda x:6 if x%2==0 else 4),
      M([59, 72, 94, 91, 79, 88, 94, 51],lambda x:x*x,lambda x:0 if x%13==0 else 5),
      M([95, 72, 78],lambda x:x+7,lambda x:7 if x%11==0 else 6),
      M([76],lambda x:x+8,lambda x:0 if x%17==0 else 2),
      M([69, 60, 53, 89, 71, 88],lambda x:x+5,lambda x:7 if x%19==0 else 1),
      M([72,54,63,80],lambda x:x+3,lambda x:1 if x%7==0 else 3)]

md_inspect = [0] * 8

for _ in range(20):
    for j,m in enumerate(md):
        md_inspect[j] += len(m.items)
        for item in m.items:
            new_worry = m.op(item)
            new_worry//=3
            md[m.test(new_worry)].items += [new_worry]
        md[j].items = []

md_inspect = sorted(md_inspect)
print(md_inspect[-1] * md_inspect[-2])

md_inspect = [0] * 8
mod_prod = 3*5*2*13*11*17*19*7

for _ in range(10000):
    for j,m in enumerate(md):
        md_inspect[j] += len(m.items)
        for item in m.items:
            new_worry = m.op(item)%mod_prod
            md[m.test(new_worry)].items += [new_worry]
        md[j].items = []

md_inspect = sorted(md_inspect)
print(md_inspect[-1] * md_inspect[-2])
