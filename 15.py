from utils import *
ls = [int(x) for x in open('15.in','r').readline().rstrip('\n').split(',')]

def one(ls):
    to_speak = deepcopy(ls)
    spoken = []
    for i in range(2020):
        if i<len(to_speak):
            spoken.append(to_speak[i])
        else:
            if spoken[-1] not in spoken[:-1]:
                spoken.append(0)
            else:
                spoken.append(spoken[:-1][::-1].index(spoken[-1])+1)
    return spoken[-1]
    
def two(ls):
    d = {}
    to_speak = deepcopy(ls)
    # spoken = []
    last = -1
    first_time = True
    last_index = 0
    for i in tqdm(range(30_000_000), unit_scale=1):
        if i<len(to_speak):
            n = to_speak[i]
        else:
            if first_time:
                n = 0
            else:
                n = d[last]-last_index
        first_time = n not in d
        if not first_time: last_index = d[n]
        d[n]=i
        last = n
    return last

if __name__ == "__main__":
    print(f"{one(ls) = }") # 
    print(f"{two(ls) = }") # 
