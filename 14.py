from utils import *
# %%
def apply_mask(num, mask):
    new_num = ''
    for i,n in enumerate(mask):
        if n in {'0','1'}:
            new_num+=n
        else:
            new_num+=num[i]
    return new_num

def one():
    mem = {}
    with open('14.in','r') as fp:
        ln = fp.readline()
        while ln:
            match = re.findall("mask \= (\S+)", ln)
            msk = match[0]
            while match:
                ln = fp.readline()
                match = re.findall("\[(\d+)\] \= (\d+)", ln)
                if match:
                    mem[match[0][0]] =  int(apply_mask(bin(int(match[0][1])).lstrip('0b').zfill(len(msk)),msk),2)
    sol = 0
    for _,v in mem.items():
        sol+=v
    return sol

# %%
def apply_mask2(num, mask):
    new_num = ''
    for i,n in enumerate(mask):
        if n == '1':
            new_num+='1'
        elif n == '0':
            new_num+=num[i]
        else:
            new_num+='X'
    nx = new_num.count('X')
    nums = []
    for poss in range(pow(2,nx)):
        digits = bin(poss).lstrip('0b').zfill(nx)
        idigit = 0
        new_addr = ''
        for d in new_num:
            if d == 'X':
                new_addr+=digits[idigit]
                idigit+=1
            else:
                new_addr+=d
        nums.append(new_addr)
    return nums

def two():
    mem = {}
    with open('14.in','r') as fp:
        ln = fp.readline()
        while ln:
            match = re.findall("mask \= (\S+)", ln)
            msk = match[0]
            while match:
                ln = fp.readline()
                match = re.findall("\[(\d+)\] \= (\d+)", ln)
                if match:
                    addr = int(match[0][0])
                    val = int(match[0][1])
                    new_addr = apply_mask2(bin(addr).lstrip('0b').zfill(len(msk)),msk)
                    for a in new_addr:
                        mem[int(a,2)] = val
    sol = 0
    for _,v in mem.items():
        sol+=v
    return sol

if __name__ == "__main__":
    print(f"{one() = }") # 15018100062885
    print(f"{two() = }") # 5724245857696
