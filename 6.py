from copy import deepcopy
q = set() #[]
ls1 = []
for s in open('6.in','r').readlines():
    for c in s:
        if c!='\n':
            q.add(c)
    if (s=='\n'):
        ls1.append(q)
        q = set()
ls1.append(q)

ls2 = []
ls3 = []
q = set()
for s in open('6.in','r').readlines():
    for c in s:
        if c!='\n':
            q.add(c)
        else:
            ls2.append(q)
            q = set()
    if (s=='\n'):
        ls3.append(deepcopy(ls2))
        ls2 = []
ls3.append(deepcopy(ls2))


def one(ls):
    tot = 0
    for l in ls:
        tot += len(l)
    return tot

def two(ls):
    tot = 0
    for setlist in ls:
        sint = setlist[0]
        for s in setlist:
            if s !=set(): sint &= s
        tot += len(sint)
    return tot
    
if __name__ == "__main__":
    print(f"{one(ls1) = }") # 6249
    print(f"{two(ls3) = }") # 3103
