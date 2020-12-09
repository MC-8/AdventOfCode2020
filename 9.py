from collections import deque

ls = []
for s in open('9.in','r').readlines():
    x = s.rstrip('\n')
    ls.append(int(x))
    

def one(ls):
    buff = deque(maxlen=25)
    i = 0
    for n in ls:
        if len(buff)==25:
            if not(any_2_sum(buff,n)==n):
                return n
            buff.popleft()
        buff.append(n)
    return 0

def any_2_sum(l,n):
    for i in range(len(l)):
        for j in range(len(l)):
            if (i!=j) and (l[i]+l[j]==n):
                return n
    return -1

def two(ls,n):
    s = deque()
    for x in ls:
        s.append(x)
        while sum(s)>n: 
            s.popleft()
        if sum(s)==n: 
            return(min(s)+max(s))
    return -1
    

if __name__ == "__main__":
    print(f"{one(ls) = }") # 1492208709
    print(f"{two(ls,one(ls)) = }") # 238243506
