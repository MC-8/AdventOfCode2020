
sids = set()

for s in open('5.in','r').readlines():
    sids.add(int(s.rstrip('\n')
                   .replace('F','0')
                   .replace('B','1')
                   .replace('L','0')
                   .replace('R','1'), 2))

def one(ls):
    # Max seat ID
    return max(ls)

def two(ls):
    # Return missing seat in range (only works if there is one missing seat only)
    # for x in range(min(ls), max(ls)+1):
    #     if x not in sids: return x, 
    #     else: return 0
    return sum(range(min(ls), max(ls)+1)) - sum(ls)
    
if __name__ == "__main__":
    print(f"{one(sids) = }") # 980
    print(f"{two(sids) = }") # 607
