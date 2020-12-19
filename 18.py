# %%
from utils import *

ls = []
ls_test = []
ls_test_results = []
ls_test_results2 = []

for line in open('18.in','r').readlines():
    ls.append([x for x in line.rstrip('\n').replace(' ','')])

for line in open('18ex.in','r').readlines():
    ls_test.append([x for x in line.rstrip('\n').replace(' ','')])

for line in open('18ex.res','r').readlines():
    ls_test_results.append(line.rstrip('\n'))

for line in open('18ex2.res','r').readlines():
    ls_test_results2.append(line.rstrip('\n'))
    
operators = {'+': lambda x,y: int(x)+int(y),
             '-': lambda x,y: int(x)-int(y),
             '*': lambda x,y: int(x)*int(y)}

def solve_simple(eq):
    e = deepcopy(eq)
    res = e[0]
    while len(e)>2:
        res = str(operators[e[1]](e[0],e[2]))
        e=[res]+e[3:]
    return res

def solve_advanced(eq):
    e = deepcopy(eq)
    res = e[0]
    plus_idx = 0
    # solve all pluses first
    while plus_idx<len(e):
        if (e[plus_idx] == '+'):
            res = str(operators['+'](e[plus_idx-1],e[plus_idx+1]))
            e=e[:max(plus_idx-1,0)]+[res]+e[plus_idx+2:]
            plus_idx = 0
        else:
            plus_idx+=1
    # then the rest
    while len(e)>2:
        res = str(operators[e[1]](e[0],e[2]))
        e=[res]+e[3:]
    return res

def do_math_on(eq):
    while len(eq)>1:
        idx = 0
        while(idx<len(eq)):
            # Solve simple while you can
            while((idx+2 < len(eq)) and (len(eq)>1) and (eq[idx].isnumeric()) and (eq[idx+2].isnumeric())):
                eq = [solve_simple(eq[idx:idx+3])]+eq[idx+3:]
            # Scan for bracket pairs, solve inner and put the result back in the equation
            if (eq[idx]=='('):
                pidx = idx
                last_open_idx = pidx
                last_close_idx = -1
                while last_close_idx<last_open_idx:
                    pidx+=1
                    if(eq[pidx]==')'):
                        last_close_idx = pidx
                    if(eq[pidx]=='('):
                        last_open_idx = pidx
                eq = eq[0:last_open_idx] + [solve_simple(eq[last_open_idx+1:last_close_idx])] + eq[last_close_idx+1:]
                idx = 0
            else:
                idx+=1
    return eq[0]

def do_math_on_advanced(eq):
    while len(eq)>1:
        idx = 0
        while(idx<len(eq)):
            # Scan for bracket pairs, solve inner and put the result back in the equation
            if (eq[idx]=='('):
                pidx = idx
                last_open_idx = pidx
                last_close_idx = -1
                while last_close_idx<last_open_idx:
                    pidx+=1
                    if(eq[pidx]==')'):
                        last_close_idx = pidx
                    if(eq[pidx]=='('):
                        last_open_idx = pidx
                eq = eq[0:last_open_idx] + [solve_advanced(eq[last_open_idx+1:last_close_idx])] + eq[last_close_idx+1:]
                idx = 0
            else:
                idx+=1
        # done with the brackets, solve the rest
        eq = [solve_advanced(eq)]
    return eq[0]
#%%
def one(ls):
    sol = 0
    for eq in ls:
        X = do_math_on(eq)
        sol += int(X)
    return sol
    
def two(ls):
    sol = 0
    for eq in ls:
        X = do_math_on_advanced(eq)
        sol += int(X)
    return sol

def test1(ls,results):
    for i,l in enumerate(ls):
        if (act:=do_math_on(l))==(exp:=results[i]):
            print(f"{i+1}: pass T1")
        else:
            print(f"{i+1}: FAIL T1, {act=}, {exp=}")

def test2(ls,results):
    for i,l in enumerate(ls):
        if (act:=do_math_on_advanced(l))==(exp:=results[i]):
            print(f"{i+1}: pass T2")
        else:
            print(f"{i+1}: FAIL T2 {act=}, {exp=}")
            
if __name__ == "__main__":
    test1(ls_test, ls_test_results)
    test2(ls_test, ls_test_results2)
    print(f"{one(ls) = }") # 131076645626
    print(f"{two(ls) = }") # 109418509151782
    pass