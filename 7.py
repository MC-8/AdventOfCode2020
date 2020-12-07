from copy import deepcopy
import itertools
import re
from collections import namedtuple

bag_pair = namedtuple('bag_pair', ['name','nr'])
rules = {}
for s in open('7.in','r').readlines():
    match = re.findall("((\S+ \S+) (?:bags? contain){1}|(\d) (\S+ \S+) (?:bags?))", s)
    rules[match[0][1]] = [bag_pair(m[3],int(m[2])) for m in match[1:] if len(match)>1]

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
