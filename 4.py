
import re
ls = []
d = {}

for s in open('4.in','r').readlines():
    pattern = "(\S+):(\S+)"
    match = re.findall(pattern, s)
    for M in match:
        k = M[0]
        v = M[1]
        d[k] = v
    if (s=='\n'):
        ls.append(d)
        d = {}
ls.append(d)

def validate_byr(x):
    return (len(x)==4) and (x.isnumeric()) and (1920<=int(x)<=2002)
    
def validate_iyr(x):
    return (len(x)==4) and (x.isnumeric()) and (2010<=int(x)<=2020)
    
def validate_eyr(x):
    return (len(x)==4) and (x.isnumeric()) and (2020<=int(x)<=2030)
    
def validate_hgt(x):
    valid = False
    if ((len(x)==4) or (len(x)==5)):
        if 'in' in x:
            valid = (59 <= int(x.rstrip('in')) <= 76)
        elif 'cm' in x:
            valid = (150 <= int(x.rstrip('cm')) <= 193)
        else:
            valid = False
    else:
        valid = False
    return valid
    
def validate_hcl(x):
    pattern = "#([a-f0-9]{6})"
    match = re.search(pattern, x)
    return match != None
    
def validate_ecl(x):
    return x in {'amb','blu','brn','gry','grn','hzl','oth'}
    
def validate_pid(x):
    return (len(x)==9) and x.isnumeric()

def validate_cid(x):
    return True

val_fun = { 'byr' : validate_byr,
            'iyr' : validate_iyr,
            'eyr' : validate_eyr,
            'hgt' : validate_hgt,
            'hcl' : validate_hcl,
            'ecl' : validate_ecl,
            'pid' : validate_pid,
            'cid' : validate_cid
           }

def one(ls):
    valid_passports = 0
    for d in ls:
        if ((len(d.keys()) == 8) or 
            ((len(d.keys()) == 7) and ('cid' not in d))):
            valid_passports += 1
    return valid_passports

def two(ls):
    valid_passports = 0
    for d in ls:
        valid = False
        if ((len(d.keys()) == 8) or 
            ((len(d.keys()) == 7) and ('cid' not in d))):
            valid = True
            for k,v in d.items():
                valid &= val_fun[k](v)
        if valid:
            valid_passports += 1
    return valid_passports
    
if __name__ == "__main__":
    print(f"{one(ls) = }") # 228
    print(f"{two(ls) = }") # 175
