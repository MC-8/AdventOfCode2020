from collections import namedtuple

ls = []
coord = namedtuple('coord',['cmd', 'n'])
for s in open('12.in','r').readlines():
    x = s.rstrip('\n')
    ls.append(coord(x[0],int(x[1:])))

bl = {'E':'N',
      'N':'W',
      'W':'S',
      'S':'E'}

br = {'N':'E',
      'W':'N',
      'S':'W',
      'E':'S'}

def one(ls):
    facing = "E"
    sE, sN = 0, 0
    for x in ls:
        if x.cmd =='L':
            for _ in range(int(x.n/90)):
                facing = bl[facing]
        elif x.cmd =='R':
            for _ in range(int(x.n/90)):
                facing = br[facing]
        elif x.cmd =='F':
            sE = sE+x.n if facing=='E' else (sE-x.n if facing=='W' else sE)
            sN = sN+x.n if facing=='N' else (sN-x.n if facing=='S' else sN)
        else:
            sE = sE+x.n if x.cmd=='E' else (sE-x.n if x.cmd=='W' else sE)
            sN = sN+x.n if x.cmd=='N' else (sN-x.n if x.cmd=='S' else sN)
    return abs(sE)+abs(sN)


def two(ls):
    wE, wN, sE, sN = 10, 1, 0, 0
    for x in ls:
        if x.cmd =='L':
            for _ in range(int(x.n/90)):
                wE,wN = -wN,wE
        elif x.cmd =='R':
            for _ in range(int(x.n/90)):
                wE,wN = wN,-wE
        elif x.cmd =='F':
            sE,sN = (sE+wE*x.n,sN+wN*x.n)
        else:
            wE = wE+x.n if (c:=x.cmd)=='E' else (wE-x.n if c=='W' else wE)
            wN = wN+x.n if (c:=x.cmd)=='N' else (wN-x.n if c=='S' else wN)
    return abs(sE)+abs(sN)


if __name__ == "__main__":
    print(f"{one(ls) = }") # 319
    print(f"{two(ls) = }") # 50157
    