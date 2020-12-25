from re import match
from utils import *

class direction(Enum):
    MOVE_U = (-1,0)
    MOVE_R = (0,1)
    MOVE_D = (1,0)
    MOVE_L = (0,-1)

def next_dir(dir: direction)->direction:
    newdir = dir
    if dir==direction.MOVE_U: newdir = direction.MOVE_R
    if dir==direction.MOVE_R: newdir = direction.MOVE_D
    if dir==direction.MOVE_D: newdir = direction.MOVE_L
    if dir==direction.MOVE_L: newdir = direction.MOVE_U
    return newdir

def next_spiral_idxs(idxs: tuple[int, int], current_dir:direction) -> tuple[int,int]:
    a,b = (x+y for x,y in zip(idxs,current_dir.value))
    return (a,b)
    
photo = {}
input_txt = open('20ex.in','r').read()
is_example = True
input_txt = open("20.in", "r").read()
is_example = False

for tile_data in input_txt.split("\n\n"):
    tile_n = tile_data.split(" ")[1].split(":")[0]
    tile_text = tile_data.split(":")[1].lstrip("\n").rstrip("\n")
    tile_map = tile_text.split("\n")
    photo[int(tile_n)] = tile_map

def count_matches(t1_map: list[str], photo: dict[int, list[str]]) -> int:
    n_match = 0
    for _, t2_map in photo.items():
        if (matches := check_match(t1_map, t2_map)) < 4:  # To Avoid match with itself
            n_match += matches
    return n_match

def is_corner_tile(tile: list[str], photo: dict[int, list[str]]):
    return count_matches(tile, photo) == 2

def rotate_tile(tile: list[str]) -> list[str]:
    # Rotates tile 90deg clockwise
    rotated_tile = []
    for new_row in range(len(tile[0])):
        row = ''
        for new_col in range(len(tile)):
            row+=tile[new_col][new_row]
        rotated_tile.append(row[::-1])
    return rotated_tile

def flip_tile(tile: list[str], up_down=False) ->list[str]:
    """Flip tile, by default left-right, or up_down when specifiying the
    optional argument"""
    flipped_tile = []
    temp_tile = deepcopy(tile)
    if up_down:
        temp_tile = rotate_tile(rotate_tile(tile))
    for row in temp_tile:
        flipped_tile.append(row[::-1])
    return flipped_tile

# Borders are:
def borders_of(tile_map: list[str]) -> tuple[str, str, str, str]:
    UP = tile_map[0]
    RIGHT = "".join(x[-1] for x in tile_map)
    DOWN = tile_map[-1]
    LEFT = "".join(x[0] for x in tile_map)
    return (UP, RIGHT, DOWN, LEFT)

def border_matches_tile(border:str, tile_map: list[str]) -> bool:
    borT = borders_of(tile_map)
    for b in borT:
        if (b == border) or (b[::-1] == border):
            return True
    return False

def check_match(tile_map1: list[str], tile_map2: list[str]) -> int:
    """Checks if any of the borders match and returns how many borders matched.
    Includes rotations and flips. Should return either 0 or 1, unless the tile is with itself, then it's 4.
    Eventually, inner tiles will have 4 matches, edge 3 matches and corners 2
    matches. Hopefully!
    """
    borT1 = borders_of(tile_map1)
    val = 0
    for b1 in borT1:
        if border_matches_tile(b1, tile_map2):
            val += 1
    assert val in [0,1,4]
    return val

def assemble_image_indexes(photo: dict[int, list[str]]) -> dict[tuple[int, int], int]:
    """Steps to build the image in an inward spiral way. Every time a tile is
    found, add it to the img_idx map.
    1) Start with a corner tile
    2) Find one adjacent tile
    3) Find next adjacent tile that matches with opposite edge
    4) If no match is found, then use the another edge (only one should match)
    """
    photo_snippets = deepcopy(photo)
    img_idx = {}
    i_col = i_row = 0
    current_tile = -1
    current_dir = direction.MOVE_R
    # 1) Find corner tile
    for tile_n, tile_map in deepcopy(photo_snippets).items():
        if is_corner_tile(tile_map, photo_snippets):
            img_idx[(i_row, i_col)] = tile_n
            photo_snippets.pop(tile_n)
            current_tile = tile_n
            break
    
    # 2) Find adjacent tile
    opposite_border = ''
    for tile_n, tile_map in deepcopy(photo_snippets).items():
        if check_match(photo[current_tile], tile_map):
            (i_row, i_col) = next_spiral_idxs((i_row, i_col),current_dir)
            img_idx[(i_row, i_col)] = tile_n
            photo_snippets.pop(tile_n)
            borders = borders_of(photo[current_tile])
            # keep border that matched, so we know what's the opposite one
            matched_border = ''
            opposite_border = ''
            for ib, b in enumerate(borders):
                if border_matches_tile(b, tile_map):
                    matched_border = b
                    break
            # Save opposite border
            borders = borders_of(tile_map)
            for ib, b in enumerate(borders):
                if b==matched_border or b[::-1]==matched_border:
                    opposite_border = borders[(ib+2)%4]
                    break
            assert (opposite_border!='')
            current_tile = tile_n
            break
    
    while photo_snippets:
        # 3) Find next adjacent tile that matches with opposite edge
        found = False
        for tile_n, tile_map in deepcopy(photo_snippets).items():
            if border_matches_tile(opposite_border, tile_map):
                # Found next tile, move on
                (i_row, i_col) = next_spiral_idxs((i_row, i_col),current_dir)
                img_idx[(i_row, i_col)] = tile_n
                photo_snippets.pop(tile_n)
                borders = borders_of(photo[current_tile])
                # keep border that matched, so we know what's the opposite one
                matched_border = ''
                opposite_border = ''
                for ib, b in enumerate(borders):
                    if border_matches_tile(b, tile_map):
                        matched_border = b
                        break
                # Save opposite border
                borders = borders_of(tile_map)
                for ib, b in enumerate(borders):
                    if b==matched_border or b[::-1]==matched_border:
                        opposite_border = borders[(ib+2)%4]
                        break
                assert (opposite_border!='')
                current_tile = tile_n
                found = True
                break
        
        if not found: 
            # 4) Opposite not found, go for any other then, then change direction
            current_dir = next_dir(current_dir)
            opposite_border = ''
            for tile_n, tile_map in deepcopy(photo_snippets).items():
                if check_match(photo[current_tile], tile_map):
                    (i_row, i_col) = next_spiral_idxs((i_row, i_col),current_dir)
                    img_idx[(i_row, i_col)] = tile_n
                    photo_snippets.pop(tile_n)
                    borders = borders_of(photo[current_tile])
                    # keep border that matched, so we know what's the opposite one
                    matched_border = ''
                    opposite_border = ''
                    for ib, b in enumerate(borders):
                        if border_matches_tile(b, tile_map):
                            matched_border = b
                            break
                    # Save opposite border
                    borders = borders_of(tile_map)
                    for ib, b in enumerate(borders):
                        if b==matched_border or b[::-1]==matched_border:
                            opposite_border = borders[(ib+2)%4]
                            break
                    assert (opposite_border!='')
                    current_tile = tile_n
                    break
    # Done, rinse and repeat!
    return img_idx




# Test
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

def build_large_image(image_idx_map:dict[tuple[int,int],int]) -> list[str]:
    large_image = []
    # go row by row assembling the large image:
    # 1) Start top left corner, image by image rotate and flip until the borders match
    # 2) Write on large image
    
    # a) determine size of image
    max_row = 0
    max_col = 0
    for k,_ in image_idx_map.items():
        row,col = k
        max_row, max_col = max(max_row, row),max(max_col, col)
    # first make sure that the tile below will match the first tile
    left_tile = deepcopy(photo[image_idx_map[(0,0)]])
    next_lower_tile = photo[image_idx_map[(1,0)]]
    done = False
    while not done:
        i = 0
        while i<4:
            bottom_border = borders_of(left_tile)[2]
            top_border = borders_of(next_lower_tile)[0]
            if bottom_border==top_border:
                done = True
                break
            elif bottom_border==top_border[::-1]:
                left_tile=flip_tile(left_tile)
                done = True
                break
            else:
                left_tile=rotate_tile(left_tile)
            i+=1
        next_lower_tile = rotate_tile(next_lower_tile)
    
    # HACK Trial and error thing to make sure the top left is correctly aligned because I'm an idiot
    # Works for the example, no need for the actual data
    if is_example:
        left_tile = flip_tile(left_tile,up_down=True)
        left_tile = flip_tile(left_tile)
        left_tile = flip_tile(left_tile,up_down=True)
    ####
    current_leftmost_tile = left_tile
    for i_row in range(max_row+1):
        right_border = borders_of(left_tile)[1] #Right border
        #  horribly inefficient and stupid but I'm tired. A MATLAB stile matrix concatenation would be so much better
        # I should not have used lists here, maybe numpy ndarrays would have been better
        tile_height = len(left_tile)
        current_row_data = {}
        for i_int_row_data in range(len(left_tile)): 
            current_row_data[i_int_row_data] = left_tile[i_int_row_data][1:-1]
            
        for i_col in range(1,max_col+1):
            right_tile = deepcopy(photo[image_idx_map[(i_row,i_col)]])
            
            i = 0
            while True:
                if i>4:
                    assert(False)
                left_border = borders_of(right_tile)[3]
                if left_border==right_border:
                    right_border = borders_of(right_tile)[1]
                    break
                elif left_border==right_border[::-1]:
                    right_tile=flip_tile(right_tile,up_down=True)
                    right_border = borders_of(right_tile)[1]
                    break
                else:
                    right_tile=rotate_tile(right_tile)
                i+=1
            for i_int_row_data in range(len(left_tile)): 
                current_row_data[i_int_row_data] += right_tile[i_int_row_data][1:-1]
        
        for i_int_row_data in range(1,len(left_tile)-1): 
            large_image.append( current_row_data[i_int_row_data] )
            
        if i_row<max_row:
            # match next left tile with the tile above it
            next_lower_tile = photo[image_idx_map[(i_row+1,0)]]
            bottom_border = borders_of(current_leftmost_tile)[2]
            i = 0
            while True:
                if i>4:
                    assert(False)
                top_border = borders_of(next_lower_tile)[0]
                if bottom_border==top_border:
                    break
                elif bottom_border==top_border[::-1]:
                    next_lower_tile=flip_tile(next_lower_tile)
                    break
                else:
                    next_lower_tile=rotate_tile(next_lower_tile)
                i+=1
        left_tile = next_lower_tile
        current_leftmost_tile = left_tile
    return large_image

def one():
    sol = 1
    for t1_num, t1_map in photo.items():
        if count_matches(t1_map, photo) == 2:
            sol = sol * t1_num
    return sol


def two():
    # I'm very tired and will solve it by hand
    sol = 0
    idxs= assemble_image_indexes(photo)
    large_image = build_large_image(idxs)
    large_image = flip_tile(large_image, up_down=True)
    print("=======================================================")
    for row in large_image: print(row)
    large_image = rotate_tile(large_image)
    print("=======================================================")
    for row in large_image: print(row)
    large_image = rotate_tile(large_image)
    print("=======================================================")
    for row in large_image: print(row)
    large_image = rotate_tile(large_image)
    print("=======================================================")
    for row in large_image: print(row)
    print("=======================================================")
    
    return sol


if __name__ == "__main__":
    print(f"{one() = }")  #
    print(f"{two() = }")  #
