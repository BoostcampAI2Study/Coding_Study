import sys, collections
N, M, K = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

tree_info = [[collections.deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, age = map(int, sys.stdin.readline().split())
    tree_info[r - 1][c - 1].append(age)

soil_info = [[5] * N for _ in range(N)]
tree_cnt = M
NR = [-1, -1, -1, 0, 0, 1, 1, 1]
NC = [-1, 0, 1, -1, 1, -1, 0, 1]

for year in range(K):
    for r in range(N):
        for c in range(N):
            dead_tree = 0
            # spring
            for i in range(len(tree_info[r][c])):
                age = tree_info[r][c].popleft()
                if age <= soil[r][c]:
                    tree_info[r][c].append(age + 1)
                    soil[r][c] -= age
                else:
                    dead_tree += age // 2
                    tree_cnt -= 1
            # summer
            soil[r][c] += dead_tree

    for r in range(N):
        for c in range(N):
            # autumn
            for age in tree_info[r][c]:
                if age % 5 == 0:
                    for i in range(8):
                        nr, nc = r + NR[i], c + NC[i]
                        if 0 <= nr < N and 0 <= nc < N:
                            tree_info[nr][nc].appendleft(1)
                            tree_cnt += 1
            # winter
            soil[r][c] += A[r][c]

print(tree_cnt)
