from copy import deepcopy
import math
import numpy as np
from collections import deque
from itertools import product

ls = []
for s in open('11.in','r').readlines():
    x = s.rstrip('\n')
    ls.append(x)

def one(lin):
    changeflag = True
    cidc = 0
    nl = []
    ls = deepcopy(lin)
    while changeflag:
        cidc += 1
        print(cidc)
        changeflag = False
        ir = 0
        ic = 0
        # print(ls)
        nl = []
        for row in ls:
            r = ""
            ic = 0
            for col in row:
                # if ic==91: continue
                # if ir==95: continue
                if (col=="L"):
                    count = 0
                    for dc,dr in product(range(-1,2,1),range(-1,2,1)):
                        if (ic+dc)==len(row): continue
                        if (ir+dr)==len(ls): continue
                        if (ir+dr)==-1: continue
                        if (ic+dc)==-1: continue
                        if (dc==dr==0): continue
                        if ls[ir+dr][ic+dc] == "#":
                            count+=1
                    if (count==0):
                        r += "#"
                        changeflag = True
                    else:
                        r += "L"
                elif (col=="#"):
                    count = 0
                    for dc,dr in product(range(-1,2,1),range(-1,2,1)):
                        if (ic+dc)==len(row): continue
                        if (ir+dr)==len(ls): continue
                        if (ir+dr)==-1: continue
                        if (ic+dc)==-1: continue
                        if (dc==dr==0): continue
                        if ls[ir+dr][ic+dc]=="#":
                            count+=1
                    if (count>=4):
                        r += "L"
                        changeflag = True
                    else:
                        r += "#"
                else:
                    r += ls[ir][ic]
                ic += 1
            # print(r)
            nl.append(r)
            ir +=1
        ls = deepcopy(nl)
        # print(nl)
    cc = 0
    for row in nl:
        for col in row:
            if col=="#":
                cc+=1
    return cc
    
def two(lin):
    changeflag = True
    cidc = 0
    nl = []
    ls = deepcopy(lin)
    while changeflag:
        cidc += 1
        print(cidc)
        changeflag = False
        ir = 0
        ic = 0
        # print(ls)
        nl = []
        for row in ls:
            r = ""
            ic = 0
            for col in row:
                # if ic==91: continue
                # if ir==95: continue
                if (col=="L"):
                    count = 0
                    for dc,dr in product(range(-1,2,1),range(-1,2,1)):
                        i = 1
                        foundflag = False
                        while not foundflag and i < 95:
                            if (i>1):
                                dc += np.sign(dc)
                                dr += np.sign(dr)
                            i+=1
                            if (ic+dc)>=len(row): break
                            if (ir+dr)>=len(ls): break
                            if (ir+dr)<0: break
                            if (ic+dc)<0: break
                            if (dc==dr==0): break
                            if ls[ir+dr][ic+dc] == "#":
                                count+=1
                            if ls[ir+dr][ic+dc] in {"#","L"}:
                                foundflag=True
                    if (count==0):
                        r += "#"
                        changeflag = True
                    else:
                        r += "L"
                elif (col=="#"):
                    count = 0
                    for dc,dr in product(range(-1,2,1),range(-1,2,1)):
                        i = 0
                        foundflag = False
                        while not foundflag and i < 95:
                            i+=1
                            if (i>1):
                                dc += np.sign(dc)
                                dr += np.sign(dr)
                            if (ic+dc)>=len(row): break
                            if (ir+dr)>=len(ls): break
                            if (ir+dr)<0: break
                            if (ic+dc)<0: break
                            if (dc==dr==0): break
                            if ls[ir+dr][ic+dc] == "#":
                                count+=1
                            if ls[ir+dr][ic+dc] in {"#","L"}:
                                foundflag=True
                    if (count>=5):
                        r += "L"
                        changeflag = True
                    else:
                        r += "#"
                else:
                    r += ls[ir][ic]
                ic += 1
            # print(r)
            nl.append(r)
            ir +=1
        ls = deepcopy(nl)
        # print(nl)
    cc = 0
    for row in nl:
        for col in row:
            if col=="#":
                cc+=1
    return cc


if __name__ == "__main__":
    # print(f"{one(ls) = }") # 
    print(f"{two(ls) = }") # 
