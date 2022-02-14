import sys

CUBE = [-1] + list(map(int, sys.stdin.readline().strip().split()))
ROTATES = [
    [1, 3, 5, 7, 9, 11, 24, 22], # Pitch
    [13, 14, 5, 6, 17, 18, 21, 22], # Roll
    [1, 2, 18, 20, 12, 11, 15, 13] # Yaw
]

def square_colored_same(cube):
    for i in range(1,24,4):
        if cube[i] == cube[i+1] == cube[i+2] == cube[i+3]: continue
        else: return False
    return True

def rotate_check():
    global CUBE, ROTATES
    
    for rotate in ROTATES:
        rotate_90, rotate_270 = rotate[2:] + rotate[:2], rotate[-2:] + rotate[:-2] # 90 rotate & -90 rotate
        new_rotate_90_cube, new_rotate_270_cube = CUBE[:], CUBE[:]

        for r, r_90 in zip(rotate, rotate_90):
            new_rotate_90_cube[r_90] = CUBE[r]
        for r, r_270 in zip(rotate, rotate_270):
            new_rotate_270_cube[r_270] = CUBE[r]
            
        if square_colored_same(new_rotate_90_cube) or square_colored_same(new_rotate_270_cube):
            return 1
    return 0

print(rotate_check())
    