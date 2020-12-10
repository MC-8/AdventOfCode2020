from copy import deepcopy
import math

ls = set()
for s in open('10.in','r').readlines():
    x = s.rstrip('\n')
    ls.add(int(x))

def one(ls):
    # Not really a tidy solution but it follows the idea that of reaching the
    # next joltage with the least available adapter
    l = deepcopy(ls)
    current_jolt = 0
    one_diffs = 0
    three_diffs = 0
    for x in range(1,max(l)+1):
        if ((current_jolt+1) in l):
            one_diffs+=1
            l.remove(current_jolt+1)
            current_jolt += 1
        elif ((current_jolt+2) in l):
            l.remove((current_jolt+2))
            current_jolt += 2
        elif ((current_jolt+3) in l):
            three_diffs+=1
            l.remove((current_jolt+3))
            current_jolt += 3
    return one_diffs*(three_diffs+1) # +1 because includes the final jump
    
def two(ls:set):
    # The explanation here is convoluted but it's like a brain dump at this point (I'm tired)
    # Possibilities are defined by how many consecutive single-jumps there are
    # that is in how many ways you can reach a certain number. if you have (0) 1
    # 4 5 6 7, you have to:
    # 1) 0 -> 1 (only one way)
    # 2) 1 -> 4 (only one way) 
    # 3) many ways to reach 7 now. 
    #   a) 4->5->6->7 
    #   b) 4->6->7 
    #   c) 4->5->7 
    #   d) 4->7
    #    There are 4 possibilities (remember 4 = pow(2,2))
    #
    # If you have 4,5,6,7,8 you'd think you can have 8 possibilities (every step
    # doubles the combinations), but since you can only jump by 3 elements, maximum, 
    # you only have 7 possibilities.
    # Imagine the steps '->n' from 4 to 8 (excluded) as bits. 
    # Then 4->5->6->7->8 "contains" 3 bits (->5, ->6, ->7). 
    # Now put a "1" to the corresponding "bit" when you remove one connection
    #  4->5->6->7->8    | 0 0 0
    #  4->5->6->8       | 0 0 1 
    #  4->5->7->8       | 0 1 0
    #  4->5->8          | 0 1 1
    #  4->6->7->8       | 1 0 0
    #  4->6->8          | 1 0 1
    #  4->7->8          | 1 1 0
    #  4->8             | 1 1 1  <-This path is not allowed because the jump is too long
    # So you have 7 solutions instead of 8
    # It's easy to see that with N intermediate steps between unique paths you can have
    # pow(2,N) combinations minus 1 for every bit from 3 bits onwards
    sl = [0] + list(ls) + [max(ls)+3]
    ones_count = []
    e = 0
    for i in range(len(sl)-1):
        if (sl[i+1]-sl[i])==1: e+=1
        else:
            if (e>1): ones_count.append(e-1)
            e = 0
            
    exps = [pow(2,x)-max(0,x-2) for x in ones_count]
    return(math.prod(exps))


if __name__ == "__main__":
    print(f"{one(ls) = }") # 2516
    print(f"{two(ls) = }") # 296196766695424
