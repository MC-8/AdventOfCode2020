# %%
from math import trunc
from utils import *

rules = {}
messages = []
re_rules = ["(\d+):([ 0-9]+)\|?([ 0-9]+)?", "(\d+): ""([ \S]+)"""]

with open('19ex.in','r') as fp:
    # l = fp.readline()
    for l in fp.readlines():
        if re.search("\d+",l):
            for rule in re_rules:
                match = re.findall(rule, l)[0]
                if (key:=int(match[0])) not in rules:
                    for i in range(len(match[1:])):
                        r = [int(x) if x.isnumeric() else x.replace('"','') for x in match[i+1].split()]
                        if r:
                            rules[key] = rules.get(key, []) + [r]
        else:
            if l!='\n': messages.append(l.strip('\n'))
    # while l!='\n':
    #     rules.append(l.rstrip('\n'))
    #     l = fp.readline()
    # l = fp.readline()
    # while l:
    #     messages.append(l.strip('\n'))
    #     l = fp.readline()
        

# #%%
# def make_chain(rules, r):
#     chain = rules[r][0]
#     subchain = []
#     for p in rules[r]:
#         for c in p:
#             subchain.append([x for x in rules[c]])
#     return subchain

def flatten(l):
    # returns a string if the elements of a list are characters, otherwise returns the list itself
    s = ''
    for x in l:
        if x=='a' or x=='b':
            s+=x
        else:
            return l
    return s
    
def resolve_rule(n):
    c = []
    if str(n) in 'ab':
        return n
    if rules[n]==[['a']] or rules[n]==[['b']]:
        return rules[n][0][0]
    for group in rules[n]:
        sc = []
        for el in group:
            sc += flatten(resolve_rule(el))
        c.append(flatten(sc))
    return [flatten(c)]

def show_rule(n):
    pass
[[['a', [[['aa', 'bb'], ['ab', 'ba']], [['ab', 'ba'], ['aa', 'bb']]], 'b']]]
print(f"{resolve_rule(0)=}")
print(f"{resolve_rule(1)=}")
print(f"{resolve_rule(2)=}")
print(f"{resolve_rule(3)=}")
print(f"{resolve_rule(4)=}")
print(f"{resolve_rule(5)=}")
print(f"{flatten('a')=}")
print(f"{flatten('a')=}")
print(f"{flatten(['a', 'b'])=}")
print(f"{flatten([['a', 'b'], ['b', 'a']])=}")

def unravel(X):
    print(f"{X=}")
    R = ''
    if not isinstance(X[0], list):
        return ''.join(y for y in X)
    else:
        for P in product(*X[0]):
            R+=unravel(list(P))
    return R
D = []
first_part = [['aa', 'bb'], ['ab', 'ba']]
second_part = [['cc', 'dd'], ['cd', 'dc']]
F = set()
for x in product(*first_part): 
    F.add(''.join(y for y in x))
print("------------------------------------------------------------")
print(F)
print("------------------------------------------------------------")
S = set()
for x in product(*second_part): 
    S.add(''.join(y for y in x))
print(S)
print("------------------------------------------------------------")
for x in product(F,S):
    print(''.join(y for y in x))
print("------------------------------------------------------------")

# print("------------------------------------------------------------")
# unravel([[['aa', 'bb'], ['ab', 'ba']], [['ab', 'ba'], ['aa', 'bb']]])
# print("------------------------------------------------------------")

print(f"{resolve_rule(0)=}")
print("------------------------------------------------------------")
print(f"{unravel(resolve_rule(0))=}")
print("------------------------------------------------------------")

def find_match(s,rr):
    mtch = True
    consumed_chars = 0
    if isinstance(rr,str):
        return s[:len(rr)]==rr,len(rr),s[len(rr):]
    else:
        while(rr or mtch):
            mtch = False
            rr_c = deepcopy(rr)
            for r in rr_c:
                m,l,_ =find_match(s,r)
                mtch|=m
                if m:
                    consumed_chars+=l
                    s=s[l:]
                    rr.remove(r)
                    break
            if not mtch: break
    return mtch,consumed_chars,s[consumed_chars:]

# s = 'abcd'
# found = True

# while found and len(s)>0:
#     found,c,s = find_match(s,'ab')
#     print((found,s,c))
    
s = 'ababbb'
found = True

r = [[['a', [[['aa', 'bb'], ['ab', 'ba']], [['ab', 'ba'], ['aa', 'bb']]], 'b']]]
while found and len(s)>0:
    found,c,s = find_match(s,r)
    print((found,s,c))
    


def one(rules, messages):
    sol = 0
    return sol
    
def two(rules, messages):
    return 0

if __name__ == "__main__":
    print(f"{one(rules, messages) = }") # 
    print(f"{two(rules, messages) = }") # 
    pass
# %%
