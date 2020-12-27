from numpy.lib.function_base import flip
from utils import *

class direction(Enum):
    U = (-1,0)
    R = (0,1)
    D = (1,0)
    L = (0,-1)

def next_dir(dir: direction)->direction:
    newdir = dir
    if dir==direction.U: newdir = direction.R
    if dir==direction.R: newdir = direction.D
    if dir==direction.D: newdir = direction.L
    if dir==direction.L: newdir = direction.U
    return newdir

def next_spiral_idxs(idxs: tuple[int, int], current_dir:direction) -> tuple[int,int]:
    a,b = (x+y for x,y in zip(idxs,current_dir.value))
    return (a,b)
    
photo = {}
# input_txt = open('20ex.in','r').read()
# is_example = True
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
    current_dir = direction.R
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



# Assemble big picture
# Pick any picture, its coordinates will be (0,0), starting picture of the big picture
# then for each remaining tile try to match them to the tiles in the big pitcure until none are left
def which_border_matches(border, tile):
    #-1 no border
    # 0,1,2,3: UP, RIGHT, DOWN, LEFT
    bt = borders_of(tile)
    for i in range(4):
        if bt[i]==border:
            return i
    return -1

def assemble_big_picture(photo: dict[int, list[str]]):
    tiles = deepcopy(photo)
    bp = {}
    # bp[(0,0,1951)] = flip_tile(photo[1951], up_down=True)
    # tiles.pop(1951)
    for k,v in deepcopy(tiles).items():
        bp[(0,0,k)] = v
        tiles.pop(k)
        break
    while tiles:
        for bp_tile_pos, bp_tile_data in deepcopy(bp).items():
            borders_bp_tile = borders_of(bp_tile_data)
            for tile_key, tile_to_match in deepcopy(tiles).items():
                # Try match normal version
                bp_tile_border_to_match = direction.U
                found = False
                for ib,b in enumerate(borders_bp_tile):
                    
                    # Try all borders of the target tile against the first tile border
                    for _ in range(4):
                        b2 = borders_of(tile_to_match)[(ib+2)%4]
                        if b==b2:
                            newx,newy = (bp_tile_pos[0] + bp_tile_border_to_match.value[0], bp_tile_pos[1] + bp_tile_border_to_match.value[1])
                            bp[(newx,newy,tile_key)] = tile_to_match
                            tiles.pop(tile_key)
                            found = True
                        tile_to_match = deepcopy(rotate_tile(tile_to_match))
                    tile_to_match = deepcopy(flip_tile(tile_to_match))
                    if not found:
                        for _ in range(4):
                            b2 = borders_of(tile_to_match)[(ib+2)%4]
                            if b==b2:
                                newx,newy = (bp_tile_pos[0] + bp_tile_border_to_match.value[0], bp_tile_pos[1] + bp_tile_border_to_match.value[1])
                                bp[(newx,newy,tile_key)] = tile_to_match
                                tiles.pop(tile_key)
                                found = True
                            tile_to_match = deepcopy(rotate_tile(tile_to_match))
                        tile_to_match = deepcopy(flip_tile(tile_to_match,up_down=True))
                    if not found:
                        for _ in range(4):
                            b2 = borders_of(tile_to_match)[(ib+2)%4]
                            if b==b2:
                                newx,newy = (bp_tile_pos[0] + bp_tile_border_to_match.value[0], bp_tile_pos[1] + bp_tile_border_to_match.value[1])
                                bp[(newx,newy,tile_key)] = tile_to_match
                                tiles.pop(tile_key)
                                found = True
                            tile_to_match = deepcopy(rotate_tile(tile_to_match))
                    # Next
                    bp_tile_border_to_match = next_dir(bp_tile_border_to_match)
    return bp

def remove_all_borders(big_picture:dict[tuple[int,int,int],list[str]]):
    tile_width = 0
    tile_height = 0
    for k,v in deepcopy(big_picture).items():
        tile_width = len(v[0])
        tile_height = len(v)
        break
    max_x=max_y=min_x=min_y=0
    for k in big_picture.keys():
        max_x = max(max_x, k[0])
        max_y = max(max_y, k[1])
        min_x = min(min_x, k[0])
        min_y = min(min_y, k[1])
    new_picture = np.chararray((((abs(max_x-min_x)+1)*(tile_height-2)), 
                          ((abs(max_y-min_y)+1))*(tile_width-2)), unicode=True)
    for xyk, tile_data in big_picture.items():
        chunk_top_left_x = (xyk[0]-min_x)*(tile_width-2)
        chunk_top_left_y = (xyk[1]-min_y)*(tile_height-2)
        td_arr = []
        for y in tile_data:
            td_arr.append([x for x in y])
        new_picture[chunk_top_left_x:chunk_top_left_x+tile_width-2,
                    chunk_top_left_y:chunk_top_left_y+tile_height-2] = np.asarray(td_arr)[1:-1,1:-1]
    return new_picture
    
monster =[
"                  # ",
"#    ##    ##    ###",
" #  #  #  #  #  #   "
]
hash_to_check = []
for ir,r in enumerate(monster):
    for ic,c in enumerate(r):
        if c=='#':
            hash_to_check.append((ir,ic))
# print(hash_to_check)

def is_monster(picture, starting_corner):
    res = True
    for coords in hash_to_check:
        r = starting_corner[0]+coords[0]
        c = starting_corner[1]+coords[1]
        res &= picture[r][c]=='#'
    return res


def one():
    sol = 1
    for t1_num, t1_map in photo.items():
        if count_matches(t1_map, photo) == 2:
            sol = sol * t1_num
    return sol


def two():
    bp = assemble_big_picture(photo)
    # print(bp)
    tp = remove_all_borders(bp)
    # print(tp)
    cols = tp[0].size
    rows = int(tp.size/cols)
    for r in range(rows):
        s = ''
        for c in range(cols):
            s+=tp[r,c]
        # print(s)
    monster_count = 0
    tpl = tp.tolist()
    i = 0
    while monster_count==0: 
        for r in range(rows-len(monster)):
            for c in range(cols-len(monster[0])):
                if is_monster(tpl, (r,c)):
                    monster_count+=1
        if monster_count==0 and i not in [4,8]:
            tpl = rotate_tile(tpl)
            # print("Rotate")
        if monster_count==0 and i==4:
            tpl = flip_tile(tpl)
            # print("Flip LR")
        if monster_count==0 and i==8:
            tpl = flip_tile(tpl, True)
            # print("Flip UD")
        i+=1
    # print(monster_count)
    # Count all '#' tiles, then subtract monster tiles
    monster_tiles = len(hash_to_check)
    hash_count = 0
    for r in range(rows):
        for c in range(cols):
            if tpl[r][c]=='#':
                hash_count+=1
    return hash_count-(monster_count*monster_tiles)


if __name__ == "__main__":
    print(f"{one() = }")  #
    print(f"{two() = }")  #