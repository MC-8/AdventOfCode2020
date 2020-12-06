ls = []
for s in open('1.in','r').readlines():
    ls.append(int(s))

def one(ls):
    ls = sorted(ls)
    for i1, num1 in enumerate(ls):
        for i2, num2 in enumerate(ls[i1+1:]):
            if (num1+num2>2020):break
            if ((i1!=i2) and (num1+num2==2020)):
                return(num1*num2)
    return -1

def two(ls):
    ls = sorted(ls)
    for i1, num1 in enumerate(ls):
        for i2, num2 in enumerate(ls[i1+1:]):
            for i3, num3 in enumerate(ls[i2+1:]):
                if (num1+num2+num3>2020):break
                if ((num1!=num2!=num3) and (num1+num2+num3==2020)):
                    return(num1*num2*num3)
    return -1

if __name__ == "__main__":
    print(f"{one(ls) = }") # 494475
    print(f"{two(ls) = }") # 267520550
