import sys
from collections import deque

input = sys.stdin.readline

near_block = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

N, M, K = map(int, input().split())

A = []
ground = [[5 for _ in range(N)] for _ in range(N)]
trees=[[deque([]) for _ in range(N)] for _ in range(N)]

for _ in range(N):
    A.append(list(map(int, input().split())))

for _ in range(M):
    r,c,age = map(int, input().split())
    trees[r-1][c-1].append(age)

for cnt in range(K):
    # spring + summer
    for r in range(N):
        for c in range(N):
            g = ground[r][c]    # 초기 땅 양분
            for _ in range(len(trees[r][c])):
                age = trees[r][c].popleft() # 일단 나무 뽑고
                if g - age >= 0:    # 양분 먹을 수 있으면 양분 먹고 다시 심어줌
                    trees[r][c].append(age+1)
                    ground[r][c]-=age; g-=age                
                else:   # 뽑은 나무 양분으로 만들어서 땅에 줌
                    ground[r][c] += (age//2)

    # fall + winter
    for r in range(N):
        for c in range(N):
            for idx, age in enumerate(trees[r][c]):
                if age % 5 == 0:
                    for (mr, mc) in near_block:
                        new_r, new_c = r+mr, c+mc
                        if 0<=new_r<N and 0<=new_c<N:
                            trees[new_r][new_c].appendleft(1)
            ground[r][c] += A[r][c]

answer=0
for r in range(N):
    for c in range(N):
        answer+=len(trees[r][c])
print(answer)