import re
from copy import deepcopy
import math
ls = []

for s in open('3.in','r').readlines():
    ls.append(s.rstrip('\n'))

def count_trees(ls, right_inc, down_inc):
    col = 0
    trees = 0
    h = len(ls)
    w = len(ls[0])
    for row in range(down_inc, h, down_inc):
        col+=right_inc
        if ls[row][col%w]=='#':
            trees +=1
    return trees

def one(ls):
    return count_trees(ls, 3, 1)

def two(ls):
    return math.prod([count_trees(ls, right_inc, down_inc) for right_inc, down_inc in zip([1,3,5,7,1],[1,1,1,1,2])])

if __name__ == "__main__":
    print(f"{one(ls) = }") # 164
    print(f"{two(ls) = }") # 5007658656
