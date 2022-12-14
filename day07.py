import sys
import re
I = sys.stdin.read().splitlines()

class D():
    def __init__(self,name,size,cd_path,dir_list):
        self.name = name
        self.size = size
        self.cd_path = cd_path
        self.dir_list = dir_list
    def update_dir(self,new_dir_name,cd_path):
        self.dir_list += ((new_dir_name,cd_path),)
    def update_size(self,more_size):
        self.size += more_size

cd_path = ()
curr_dir = ""
dirs = {}
for i in I:
    if i[0] == "$":
        if i[2] == "c": # cd
            curr_dir = re.findall(r"\$ cd (.+)",i)[0]
            if curr_dir == "..": # cd ..
                cd_path = cd_path[:-1]
                curr_dir = cd_path[-1]
            else: # cd (dir)
                cd_path += (curr_dir,)
                dirs[(curr_dir,cd_path)] = D(curr_dir,0,cd_path,tuple())
    else:
        if i[0] == "d": # dir
            child_dir = re.findall(r"dir (.+)",i)[0]
            dirs[(curr_dir,cd_path)].update_dir(child_dir,cd_path+(child_dir,))
        else: # file
            x = re.findall(r"(\d+)",i)[0]
            dirs[(curr_dir,cd_path)].update_size(int(x))

def dir_sum(d):
    if d.dir_list:
        return sum(dir_sum(dirs[x]) for x in d.dir_list) + d.size
    else:
        return d.size

dir_sums = []
unused = 0
for i in dirs.values():
    curr = dir_sum(i)
    if i.name == "/":
        unused = 70000000 - curr
    dir_sums += [curr]

need_to_free = 30000000 - unused

part1 = [x for x in dir_sums if x<=100000]
part2 = [x for x in dir_sums if x>need_to_free]
print(sum(part1))
print(min(part2))
