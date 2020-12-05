
ls = set() #[]

for s in open('6.in','r').readlines():
    ls.add(int(s.rstrip('\n')
                .replace('F','0')
                .replace('B','1')
                .replace('L','0')
                .replace('R','1'), 2))

def one(ls):
    return -1

def two(ls):
    return -1
    
if __name__ == "__main__":
    print(f"{one(ls) = }") # 980
    print(f"{two(ls) = }") # 607
