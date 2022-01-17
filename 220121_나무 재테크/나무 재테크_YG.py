from collections import defaultdict
import sys

input = sys.stdin.readline

# N = 땅 크기, M = 나무 수, K = 햇수
N, M, K = map(int, input().split())

# A 입력
A = [list(map(int, input().split())) for _ in range(N)]

# 나무 정보 입력 key=나이, value = 위치담긴 리스트
trees = defaultdict(list)
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[z].append((x-1, y-1))

# 봄: 나무가 자신의 나이만큼 양분을 먹고 나이가 +1. 나이가 어린 나무부터 양분을 먹고 못먹으면 die
# 여름: 봄에 죽은 나무가 양분으로 변함. 나이//2가 양분으로 추가된다.
# 가을: 나무가 번식한다. 나이가 5의 배수여야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
# 겨울: S2D2가 땅에 양분을 추가.

# 인접한 8개 칸
dx =[1,1,0,-1,-1,-1,0,1]
dy =[0,-1,-1,-1,0,1,1,1]

# 초기 양분 5로 초기화
yangboon = [[5]*N for _ in range(N)]

# K년동안 진행
for year in range(K):
    dying = defaultdict(list)

    # 봄
    new_trees = defaultdict(list)
    # 나이 어린애들부터
    for age in sorted(list(trees.keys())):
        for x, y in trees[age]:
            if yangboon[x][y] >= age:
                new_trees[age+1].append((x, y))
                yangboon[x][y] -= age
            else:
                dying[age].append((x, y))
    trees = new_trees

    # 여름
    for die in dying:
        for x, y in dying[die]:
            yangboon[x][y] += die//2

    # 가을
    address = []
    for age in trees:
        if age % 5 == 0:
            address += trees[age]

    for x, y in address:
        for k in range(8):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                trees[1].append((nx, ny))

    # 겨울
    for a in range(N):
        for b in range(N):
            yangboon[a][b] += A[a][b]

# 답 출력
answer = sum(map(len, list(trees.values())))
print(answer)