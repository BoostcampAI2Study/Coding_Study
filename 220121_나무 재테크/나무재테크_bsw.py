N, M, K = map(int, input().split())

# 해마다 추가되는 양분
B=[]
for _ in range(N):
    B.append(list(map(int, input().split())))

# 처음 땅
A = [[5]*N for _ in range(N)]

trees=[[[] for _ in range(len(A[0]))] for _ in range(N)]
graves=[[[] for _ in range(len(A[0]))] for _ in range(N)]
for _ in range(M):
    r, c, y = map(int, input().split())

    trees[r-1][c-1].append(y)


def spring():
    for r, row in enumerate(trees):
        for c, col in enumerate(row):
            if not col:
                continue
            trees[r][c].sort()
            for i, tree in enumerate(col):
                if tree > A[r][c] :
                    graves[r][c].extend(trees[r][c][i:])
                    trees[r][c] = trees[r][c][:i]
                    break
                else:
                    A[r][c] -= tree
                    trees[r][c][i] += 1


def summer():
    for r, row in enumerate(graves):
        for c, col in enumerate(row):
            if not col :
                continue
            for _, tree in enumerate(col):
                A[r][c] += tree//2
            graves[r][c] = []


def autumn():
    next = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    N, M = len(trees), len(trees[0])
    for r in range(N):
        for c in range(M):
            for tree in trees[r][c]:
                if tree % 5 == 0:    
                    for dr, dc in next:
                        nr, nc = r+dr, c+dc

                        if 0<=nr<N and 0<=nc<M:
                            trees[nr][nc].append(1)


def winter():
    N, M = len(trees), len(trees[0])
    
    for r in range(N):
        for c in range(M):
            A[r][c] += B[r][c]


def main():
    for _ in range(K):
        spring()
        summer()
        autumn()
        winter()

    ans=0
    for r in range(N):
        for c in range(N):
            ans += len(trees[r][c])

    print(ans)


main()
