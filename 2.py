import re
ls = []
for s in open('2.in','r').readlines():
    ls.append(s)

def one(ls):
    valid = 0

    for l in ls:
        pattern = "(\d+)-(\d+) (\S{1}): (\S+)"
        match = re.search(pattern, l)
        min_occ = int(match[1])
        max_occ = int(match[2])
        letter = match[3]
        password = match[4]
        if (min_occ <= password.count(letter) <= max_occ):
            valid+=1

    return valid

def two(ls):
    valid = 0

    for l in ls:
        pattern = "(\d+)-(\d+) (\S{1}): (\S+)"
        match = re.search(pattern, l)
        min_occ = int(match[1])
        max_occ = int(match[2])
        letter = match[3]
        password = match[4]
        if ((password[min_occ-1]==letter) ^ (password[max_occ-1]==letter)):
            valid+=1

    return valid

if __name__ == "__main__":
    print(f"{one(ls) = }") # 603
    print(f"{two(ls) = }") # 404
