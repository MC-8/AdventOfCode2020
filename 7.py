from copy import deepcopy
import itertools
import re
from collections import namedtuple

bag_pair = namedtuple('bag_pair', ['name','nr'])
d = {}
rules = {}
allbags = set()
for s in open('7.in','r').readlines():
    pattern = "^(\S+ \S+){1}"
    match = re.search(pattern, s)
    parent = match[0]
    pattern = "(\d \S+ \S+ bags?)"
    match = re.findall(pattern, s)
    children = []
    for m in match:
        l = m.split() # "4 drab silver bags" -> ['4','drab','silver','bags']
        child = bag_pair(l[1]+' '+l[2],int(l[0])) # ("drab silver", 4)
        children.append(child)
    rules[parent] = children

def one():
    wcsg = set() # who contains shiny gold?
    repeat = True
    to_find = {"shiny gold"}
    while repeat:
        repeat = False
        for r in rules:
            for c in rules[r]:
                if c.name in to_find and r not in to_find:
                    wcsg.add(r)
                    to_find.add(r)
                    repeat = True
    return len(wcsg)

# Recursive way to solve first part, 50x slower :/
# def eventually_contains(entry, bag):
#     retval = False
#     for r in rules[entry]:
#         if r.name==bag: return True
#         retval = eventually_contains(r.name, bag)
#         if retval: return True
#     return retval

def count_bags_in(bag):
    bags = 0
    for r in rules[bag]:
        bags += r.nr*(1 + count_bags_in(r.name))
    return bags

def two():
    return count_bags_in("shiny gold")
    

if __name__ == "__main__":
    print(f"{one() = }") # 103
    print(f"{two() = }") # 1469
