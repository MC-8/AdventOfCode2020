from utils import *

space = {}
with open('17.in','r') as fp:
    lines = fp.readlines()
    for x,y in product(range(len(lines[0].rstrip('\n'))),range(len(lines))):
        space[(x,y,0,0)] = lines[y][x]

def augment(space):
    new_space = {}
    spc = deepcopy(space)
    for coord,cube in space.items():
        for d in product(*[(1,0,-1) for _ in range(len(coord))]):
            nc=tuple(coord+np.array(d))
            if (nc not in space.keys()):
                new_space[nc]='.'
            elif d==tuple([0 for _ in range(len(coord))]):
                new_space[nc]=cube
    return new_space
def pad(some_tuple:tuple, max_len:int, pad_char:int=0)->tuple:
    return some_tuple+(pad_char,)*(max_len-len(some_tuple))
    
def scan_space(space,n_dim):
    space = deepcopy(space)
    space = augment(space)
    next_space = {}
    count_active = 0
    for coord,cube in tqdm(space.items()):
        neighbors = 0
        for d in product(*[(1,0,-1) for _ in range(n_dim)]):
            if space.get(tuple(coord+np.array(pad(d,len(coord)))),None)=='#' and d!=pad((0,),n_dim):
                neighbors+=1
        if cube=='#':
            if (2<=neighbors<=3):
                if coord not in next_space.keys():
                    count_active+=1
                next_space[coord] = '#'#
            else: 
                next_space[coord] = '.'
        elif cube=='.':
            if (neighbors==3):
                if coord not in next_space.keys():
                    count_active+=1
                next_space[coord] = '#'#
            else: 
                next_space[coord] = '.'
    return count_active, next_space

def one(s):
    ns = deepcopy(s)
    active = 0
    for _ in range(6):
        active, ns = scan_space(ns,3)
    return active

def two(s):
    ns = deepcopy(s)
    active = 0
    for _ in range(6):
        active, ns = scan_space(ns,4)
    return active


if __name__ == "__main__":
    print(f"{one(space) = }") # 362
    print(f"{two(space) = }") # 1980
