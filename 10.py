from copy import deepcopy
import itertools
import re
from collections import namedtuple
from matplotlib import pyplot as plt
import math

ls = set()
for s in open('10.in','r').readlines():
    x = s.rstrip('\n')
    ls.add(int(x))


def one(ls):
    l = deepcopy(ls)
    current_jolt = 0
    one_diffs = 0
    three_diffs = 0
    for x in range(1,max(l)+1):
        if ((current_jolt+1) in l):
            one_diffs+=1
            l.remove(current_jolt+1)
            current_jolt += 1
        elif ((current_jolt+2) in l):
            l.remove((current_jolt+2))
            current_jolt += 2
        elif ((current_jolt+3) in l):
            three_diffs+=1
            l.remove((current_jolt+3))
            current_jolt += 3
    return one_diffs*(three_diffs+1)

def valid_sequence(ls):
    l = deepcopy(ls)
    current_jolt = 0
    # while True:
    ml = max(l)
    for _ in range(len(l)):
        if ((current_jolt+1) in l):
            l.remove(current_jolt+1)
            current_jolt += 1
        elif ((current_jolt+2) in l):
            l.remove((current_jolt+2))
            current_jolt += 2
        elif ((current_jolt+3) in l):
            l.remove((current_jolt+3))
            current_jolt += 3
        # else: return False
    if current_jolt==ml:
        return True
    else:
        return False

def count_jumps(ls):
    l = deepcopy(ls)
    current_jolt = 0
    jumps = 0
    sl = sorted([x for x in l])
    removables = set()
    for x in sl:
        if ((x+2) in sl):
            if (x+1) in sl:
                jumps+=1
                print(f"{x+1} can be removed")
                removables.add(x+1)
        if ((x+3) in sl):
            if (x+1) in sl:
                jumps+=1
                print(f"{x+1} can be removed")
                removables.add(x+1)
            if (x+2) in sl:
                jumps+=1
                print(f"{x+2} can be removed")
                removables.add(x+2)
    return len(removables)
    
def twos(ls):
    l = deepcopy(ls)
    sl = sorted([x for x in l])
    combinations_exp = 0
    sl.append(max(sl)+3)
    exps = []
    e = 0
    for x in (sl[:-1]):
        if valid_sequence(set(sl) ^ {x}):
            combinations_exp+=1
            print(f"Removing {x} OK")
            e += 1
        else:
            print(f"Removing {x} NO")
            exps.append(e)
            e = 0
    print(f"{exps=}")
    possbs = [pow(2,x) if (x<3) else pow(2,x)-(x-2) for x in exps] # 296196766695424 296196766695424
    possbs = [pow(2,x)-max(0,x-2) for x in exps]
    print(f"{possbs=}")
    return math.prod(possbs)
    
def two(ls:set):
    # The explanation here is convoluted but it's like a brain dump at this point (I'm tired)
    # Possibilities are defined by how many consecutive single-jumps there are
    # that is in how many ways you can reach a certain number. if you have (0) 1
    # 4 5 6 7, you have to:
    # 1) 0 -> 1 (only one way)
    # 2) 1 -> 4 (only one way) 
    # 3) many ways to reach 7 now. 
    #   a) 4->5->6->7 
    #   b) 4->6->7 
    #   c) 4->5->7 
    #   d) 4->7
    #    There are 4 possibilities (remember 4 = pow(2,2))
    #
    # If you have 4,5,6,7,8 you'd think you can have 8 possibilities (every step
    # doubles the combinations), but since you can only jump by 3 elements, maximum, 
    # you only have 7 possibilities.
    # Imagine the steps '->n' from 4 to 8 (excluded) as bits. 
    # Then 4->5->6->7->8 "contains" 3 bits (->5, ->6, ->7). 
    # Now put a "1" to the corresponding "bit" when you remove one connection
    #  4->5->6->7->8    | 0 0 0
    #  4->5->6->8       | 0 0 1 
    #  4->5->7->8       | 0 1 0
    #  4->5->8          | 0 1 1
    #  4->6->7->8       | 1 0 0
    #  4->6->8          | 1 0 1
    #  4->7->8          | 1 1 0
    #  4->8             | 1 1 1  <-This path is not allowed because the jump is too long
    # So you have 7 solutions instead of 8
    # It's easy to see that with N intermediate steps between unique paths you can have
    # pow(2,N) combinations minus 1 for every bit from 3 bits onwards
    sl = [0] + list(ls) + [max(ls)+3]
    ones_count = []
    e = 0
    for i in range(len(sl)-1):
        if (sl[i+1]-sl[i])==1: e+=1
        else:
            if (e>1): ones_count.append(e-1)
            e = 0
            
    exps = [pow(2,x)-max(0,x-2) for x in ones_count]
    return(math.prod(exps))


if __name__ == "__main__":
    print(f"{one(ls) = }") # 2516
    print(f"{two(ls) = }") # 296196766695424
