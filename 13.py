# %%
import pretty_errors
from collections import namedtuple
from re import S
from pulp import LpMinimize, LpProblem, PULP_CBC_CMD, LpStatus, lpSum, LpVariable, LpInteger
from math import lcm, prod
from copy import deepcopy
from pulp.utilities import allcombinations

pretty_errors.configure(
    separator_character = '*',
    filename_display    = pretty_errors.FILENAME_EXTENDED,
    line_number_first   = True,
    display_link        = True,
    lines_before        = 5,
    lines_after         = 2,
    line_color          = pretty_errors.RED + '> ' + pretty_errors.default_config.line_color,
    code_color          = '  ' + pretty_errors.default_config.line_color,
)

ls = []
# %%
L = open('13.in','r').readlines()
# L = open('13ex.in','r').readlines()
L = open('13ex2.in','r').readlines()
T = int(L[0].rstrip('\n'))
tt = [int(x) for x in L[1].rstrip('\n').replace('x','0').split(',')]

# %%
def one():
    wait_time = 1e9
    bus_nr = 0
    for bus_line in tt:
        new_wait = bus_line - T%bus_line if bus_line!=0 else 1e9
        if new_wait < wait_time:
            wait_time = new_wait
            bus_nr = bus_line
    return bus_nr*wait_time


def two():
    # tt value is bus line, and its index is the offset
    ##################################################################
    # model = LpProblem(name="example-problem", sense=LpMinimize)
    # x1 = LpVariable(name="x1", lowBound=1, cat=LpInteger)
    # x2 = LpVariable(name="x2", lowBound=1, cat=LpInteger)
    # x3 = LpVariable(name="x3", lowBound=1, cat=LpInteger)
    # x4 = LpVariable(name="x4", lowBound=1, cat=LpInteger)
    # model += (x1 - 17*x2 == 0)
    # model += (x1 - 13*x3 == -2)
    # model += (x1 - 19*x4 == -3)
    # model += (x1 <= lcm(17,13,19))
    # model += x1 # obj_function
    ##################################################################
    model = LpProblem(name="part2-problem", sense=LpMinimize)
    sol = LpVariable(name="sol", lowBound=1, cat=LpInteger)
    xx = []
    times_lcm = lcm(*[y for y in tt if y>0])
    print(f"{prod([y for y in tt if y>0])=}")
    for i,b in enumerate(tt):
        if b>0:
            x = LpVariable(name="x"+str(b),
                           lowBound=1,
                        #    upBound=times_lcm/b,
                           cat=LpInteger)
            xx.append((b,x,i))
    for eq in xx:
        model += (sol - eq[0]*eq[1] == -eq[2])
    model += (sol <= lcm(*[y for y in tt if y>0]))
    model += (sol >= 0)
    model += sol
    
    # Solve the optimization problem
    status = model.solve(PULP_CBC_CMD(msg=0)) # Set msg to 1 to print solver steps
    # print(f"status: {model.status}, {LpStatus[model.status]}")
    # print(f"objective: {model.objective.value()}")

    # for var in model.variables():
    #     print(f"{var.name}: {var.value()}")

    # for name, constraint in model.constraints.items():
    #     print(f"{name}: {constraint.value()}")
    return int(model.objective.value())

def ok_mod(base,n,mod,mod_base):
    x = n*int(base/n)+n
    return (x%mod_base)==mod,n

def ok_mod2(base,n,mod,mod_base):
    #x = n*int(base/n)+n
    if base<n: 
        return False,n
    else:
        return ((base+mod)%n)==0,n

def ok_mod_vis(base,n,mod,mod_base):
    #x = n*int(base/n)+n
    if base<n: 
        return False,n
    else:
        return ((base+mod)%n)==0,n

def two2():
    bus_offset_pairs = []
    for i,b in enumerate(tt):
        if b>0:
            bus_offset_pairs.append((b,i))
    allmods_ok = False
    starting = 0
    base = starting#-starting%bus_offset_pairs[0][0]# 0#bus_offset_pairs[0][0]
    i=base
    succ_jmp = set()
    to_jmp = set([b for b in bus_offset_pairs])
    tmp_jmp = deepcopy(to_jmp)
    while not allmods_ok or base==0:
        allmods_ok = True
        failed_incs = []
        success_incs = []
        for bop in bus_offset_pairs:
            res, inc_base = ok_mod2(base, bop[0], bop[1],bus_offset_pairs[0][0])
            if not res: 
                failed_incs.append(inc_base)
            if res: 
                success_incs.append(inc_base)
                succ_jmp.add(inc_base)
                # tmp_jmp.remove(bop)
            allmods_ok &= res
        to_jmp = deepcopy(tmp_jmp)
        print(f"{base:,} + {prod(succ_jmp)} | {success_incs} | {succ_jmp}")
        pstr = []
        # for x in bus_offset_pairs:
        #     if x[0] in success_incs:
        #         pstr.append('D')
        #     else:
        #         pstr.append('.')
        # print(f"{i}\t{pstr}")
        if i==1068797:
            return
        if not allmods_ok:
            base+= prod(succ_jmp)
            # base +=1789# inc_base
        i+=1
    print(f"Done in {i} iterations")
    return base

if __name__ == "__main__":
    print(f"{one() = }") #
    # print(f"{two() = }") #
    print(f"{two2() = }") #
