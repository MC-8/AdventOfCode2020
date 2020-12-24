# %%
from utils import *

rules = {}
messages = []
re_rules = ["(\d+):([ 0-9]+)\|?([ 0-9]+)?", "(\d+): ""([ \S]+)"""]

with open('19.in','r') as fp:
    # This parsing is ugly, next time try using splitlines() to isolate first part from second
    # And avoid regex, just split by characters :,| etc
    for l in fp.readlines():
        if re.search("\d+",l):
            for rule in re_rules:
                match = re.findall(rule, l)[0]
                if (key:=int(match[0])) not in rules:
                    for i in range(len(match[1:])):
                        r = [int(x) if x.isnumeric() else x.replace('"','') for x in match[i+1].split()]
                        if r:
                            if r==['a'] or r==['b']:
                                rules[key] = r[0]
                            else:
                                rules[key] = rules.get(key, []) + [r]
        else:
            if l!='\n': messages.append(l.strip('\n'))

def resolve_rule(n,rules,cache={}):
    if n in cache: return cache[n]
    r = rules[n]
    if isinstance(r,str): return r
    sc = []
    for group in rules[n]:
        T = [resolve_rule(x,rules,cache) for x in group]
        sc += [''.join(x) for x in product(*T)]
    cache[n] = sc
    return sc

def resolve_rule2(n,rules,cache={}):
    if n in cache: return cache[n]
    r = rules[n]
    if isinstance(r,str): return r
    sc = []
    for group in rules[n]:
        T = [resolve_rule2(x,rules,cache) for x in group]
        sc += [''.join(x) for x in product(*T)]
    cache[n] = sc
    return sc

def one(rules):
    sol = 0
    rr = set(resolve_rule(0,rules,{}))
    for msg in messages:
        if msg in rr:
            sol+=1
    return sol
    
def two(rules):
    sol = 0
    # 0: 8 11
    # 8: 42 | 8
    # 11: 42 31 | 42 11 31
    # Which means that the strings would be composed by
    # [1..N] chunks of rule[42]
    # Then [1..M] chunks of rule[31]
    
    r42 = resolve_rule(42, rules)
    r31 = resolve_rule(31, rules)
    len42 = len(r42[0]) # assumes all chunks have equal length
    len31 = len(r31[0]) # assumes all chunks have equal length
    
    # # Use sets for speed
    # r42 = set(r42)
    # r31 = set(r31)
    for msg in messages:
        # Count M+N instances of r42 from the beginning and must satisfy NM>N>0
        M = 0
        NM = 0
        while msg:
            if msg[:len42] in r42:
                msg = msg[len42:]
                NM+=1
            else:
                break
        # Next, count M instances of r31 from the end of the last
        while msg:
            if msg[:len31] in r31:
                msg = msg[len31:]
                M+=1
            else: 
                break
        # Match if NM>N>0 and we read the whole message till the end
        if NM>M>0 and not msg:
            sol+=1
    return sol

if __name__ == "__main__":
    print(f"{one(rules) = }") # 226
    print(f"{two(rules) = }") # 355
# %%
