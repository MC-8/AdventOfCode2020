from utils import *
photo = {}
# input_txt = open('20ex.in','r').read()
input_txt = open('20.in','r').read()

for tile_data in input_txt.split('\n\n'):
    tile_n = tile_data.split(' ')[1].split(':')[0]
    tile_text = tile_data.split(':')[1].lstrip('\n').rstrip('\n')
    tile_map = tile_text.split('\n')
    photo[int(tile_n)] = tile_map

# Borders are:
def borders_of(tile_map: list[str]) -> tuple[str,str,str,str]:
    UP = tile_map[0]
    RIGHT = ''.join(x[-1] for x in tile_map)
    DOWN = tile_map[-1]
    LEFT = ''.join(x[0] for x in tile_map)
    return (UP, RIGHT, DOWN, LEFT)


def check_match(tile_map1:list[str], tile_map2:list[str]) -> int:
    """Checks if any of the borders match and returns how many borders matched.
    Includes rotations and flips. Should return either 0 or one, hopefully.
    Eventually, inner tiles will have 4 matches, edge 3 matches and corners 2
    matches. Hopefully!
    """
    borT1 = borders_of(tile_map1)
    borT2 = borders_of(tile_map2)
    val = 0
    for b1 in borT1:
        for b2 in borT2:
            if b2==b1:
                val+=1
            if b2==b1[::-1]: # flipped version
                val+=1
    assert(val in range(5))
    return val

def assemble_image_indexes(photo:dict[int,list[str]]) -> dict[tuple[int,int],int]:
    """Steps to build the image in an inward spiral way. Every time a tile is
    found, add it to the img_idx map.
    1) Start with a corner tile
    2) Find one adjacent tile
    3) Find next adjacent tile that matches with opposite edge
    4) If no match is found, then use the another edge (only one should match)
    """
    img_idx = {}
    i_col = i_row = 0
    
    return img_idx

def is_corner_tile(tile: list[str], photo: dict[int, list[str]]):
    return count_matches(tile, photo)==2

### Test
# # 1951    2311    3079
# # 2729    1427    2473
# # 2971    1489    1171
# T_N = [ 1951, 2311, 3079,
#         2729, 1427, 2473,
#         2971, 1489, 1171]
# to_check = 2
# check_match(photo[T_N[to_check]],photo[2473])
# for T in T_N:
#     print(f"{T_N[to_check]} with {T}: {check_match(photo[T_N[to_check]],photo[T])}")
# # With to_check = 0
# # 1951 with 1951: 4
# # 1951 with 2311: 1
# # 1951 with 3079: 0
# # 1951 with 2729: 1
# # 1951 with 1427: 0
# # 1951 with 2473: 0
# # 1951 with 2971: 0
# # 1951 with 1489: 0
# # 1951 with 1171: 0
# # Looks good. Time to do it for real
###
def count_matches(t1_map: list[str], photo: dict[int,list[str]]) -> int:
    n_match = 0
    for _, t2_map in photo.items():
        if ((matches:=check_match(t1_map, t2_map)) < 4): # To Avoid match with itself
            n_match+=matches
    return n_match

def one():
    sol = 1
    for t1_num, t1_map in photo.items():
        if count_matches(t1_map, photo)==2:
            sol = sol*t1_num
    return sol
    
def two():
    sol = 0
    return sol


if __name__ == "__main__":
    print(f"{one() = }") # 
    print(f"{two() = }") # 
