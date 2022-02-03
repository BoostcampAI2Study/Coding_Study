import sys
import copy

input = sys.stdin.readline

cube = list(map(int, input().split()))

cube = [-1]+cube

def check(cub):
    idx1 = 1
    idx2 = 5
    for k in range(6):
        if len(set(cub[idx1:idx2])) != 1:
            return False
            break
        idx1 += 4
        idx2 += 4
    else:
        return True

# 노가다...
# 세로

# 왼쪽 밑으로
ncube = copy.deepcopy(cube)
ncube[1], ncube[3], ncube[5], ncube[7], ncube[9], ncube[11], ncube[22], ncube[24] \
= ncube[22], ncube[24], ncube[1], ncube[3], ncube[5], ncube[7], ncube[9], ncube[11]

if check(ncube):
    print(1)
    sys.exit()

# 왼쪽 위로
ncube = copy.deepcopy(cube)
ncube[1], ncube[3], ncube[5], ncube[7], ncube[9], ncube[11], ncube[22], ncube[24] \
= ncube[5], ncube[7], ncube[9], ncube[11], ncube[22], ncube[24], ncube[1], ncube[3]

if check(ncube):
    print(1)
    sys.exit()


# 가로
# 위쪽 왼쪽으로
ncube = copy.deepcopy(cube)
ncube[13], ncube[14], ncube[5], ncube[6], ncube[17], ncube[18], ncube[21], ncube[22] \
 = ncube[5], ncube[6], ncube[17], ncube[18], ncube[21], ncube[22] ,ncube[13], ncube[14]

if check(ncube):
    print(1)
    sys.exit()

# 위쪽 오른쪽으로
ncube = copy.deepcopy(cube)
ncube[13], ncube[14], ncube[5], ncube[6], ncube[17], ncube[18], ncube[21], ncube[22] \
 = ncube[21], ncube[22], ncube[13], ncube[14], ncube[5], ncube[6] ,ncube[17], ncube[18]

if check(ncube):
    print(1)
    sys.exit()

# 위, 아래
ncube = copy.deepcopy(cube)
ncube[3], ncube[4], ncube[14], ncube[16], ncube[9], ncube[10], ncube[17], ncube[19] \
 = ncube[17], ncube[19], ncube[3], ncube[4], ncube[14], ncube[16] ,ncube[9], ncube[10]

if check(ncube):
    print(1)
    sys.exit()

ncube = copy.deepcopy(cube)
ncube[3], ncube[4], ncube[14], ncube[16], ncube[9], ncube[10], ncube[17], ncube[19] \
 = ncube[14], ncube[16], ncube[9], ncube[10], ncube[17], ncube[19] ,ncube[3], ncube[4]

if check(ncube):
    print(1)
    sys.exit()

# 모든 경우 안되면 0 출력
print(0)