from utils import *

ls = []
# %%
L = open('13.in','r').readlines()
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


def two_simplex():
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
    for i,b in enumerate(tt):
        if b>0:
            x = LpVariable(name="x"+str(b),
                           lowBound=1,
                        #    upBound=lcm(*[y for y in tt if y>0])/b,
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

def ok_mod(base,n,mod):
    if base<n: 
        return False,n
    else:
        return ((base+mod)%n)==0,n

def two():
    bus_offset_pairs = []
    for i,b in enumerate(tt):
        if b>0:
            bus_offset_pairs.append((b,i))
    allmods_ok = False
    base = 0
    succ_base = set()
    to_jmp = set([b for b in bus_offset_pairs])
    tmp_jmp = deepcopy(to_jmp) # Reduce n of iterations if we avoid checking mods for steps we already did.
    while not allmods_ok:
        allmods_ok = True
        for bop in to_jmp:
            res, inc_base = ok_mod(base, bop[0], bop[1])
            if res: 
                succ_base.add(inc_base)
                tmp_jmp.remove(bop)
            allmods_ok &= res
        to_jmp = deepcopy(tmp_jmp)
        if not allmods_ok:
            base+= prod(succ_base)
    return base

if __name__ == "__main__":
    print(f"{one() = }") # 2298
    print(f"{two() = }") # 783685719679632
