from copy import deepcopy
import itertools
import re
from collections import namedtuple

ls = []
for s in open('8.in','r').readlines():
    x = s.rstrip('\n').split(' ')
    ls.append((x[0],int(x[1])))
    

def one(ls):
    acc = 0
    idx = 0
    ni = ls[idx]
    executed = set()
    while idx not in executed:
        if ls[idx][0] == 'acc':
            acc+= ls[idx][1]
            executed.add(idx)
            idx+=1
        elif ls[idx][0] == 'nop':
            executed.add(idx)
            idx+=1
        elif ls[idx][0] == 'jmp':
            executed.add(idx)
            idx+=ls[idx][1]
    return acc

def run_and_change(l, idx_c):
    ls = deepcopy(l)
    if ls[idx_c][0] == 'nop':
        ls[idx_c] = ('jmp', ls[idx_c][1])
    if ls[idx_c][0] == 'jmp':
        ls[idx_c] = ('nop', ls[idx_c][1])
    acc = 0
    idx = 0
    ni = ls[idx]
    li = idx
    executed = set()
    while (idx<len(ls) and idx not in executed) or idx==(len(ls)-1):
        if ls[idx][0] == 'acc':
            acc+= ls[idx][1]
            executed.add(idx)
            li = idx
            idx+=1
        elif ls[idx][0] == 'nop':
            executed.add(idx)
            li = idx
            idx+=1
        elif ls[idx][0] == 'jmp':
            executed.add(idx)
            li = idx
            idx+=ls[idx][1]
    return acc,li
    
def two(ls):
    for x in range(len(ls)-1):
        acc,idx = run_and_change(ls, x)
        if idx==(len(ls)-1): return acc
    return 0
    

if __name__ == "__main__":
    print(f"{one(ls) = }") # 1217
    print(f"{two(ls) = }") # 501
