N, M, K = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(N)]
tree_info = [[int(i) for i in input().split()] for _ in range(M)]
tree_info = [[r - 1, c - 1, age] for r, c, age in tree_info]

soil_info = [[5] * N for _ in range(N)]
cur_tree, new_tree, die_tree = [], [], []
NR = [-1, -1, -1, 0, 0, 1, 1, 1]
NC = [-1, 0, 1, -1, 1, -1, 0, 1]

tree_info.sort()
for year in range(K):
    for idx in range(len(tree_info)):
        r, c, age = tree_info[idx]
        # 봄
        if soil_info[r][c] >= age:
            soil_info[r][c] -= age
            cur_tree.append([r, c, age + 1])
            # 새로운 나무
            if (age+1) % 5 == 0:
                for i in range(8):
                    nr, nc = NR[i] + r, NC[i] + c
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        continue
                    new_tree.append([nr, nc, 1])
        else:
            die_tree.append([r, c, age//2])         # 나무 죽음

    tree_info = cur_tree[:]
    # 여름
    for r, c, age in die_tree:
        soil_info[r][c] += age
    # 새나무 심기
    tree_info = new_tree + tree_info
    # 겨울
    soil_info = [[soil_info[r][c] + A[r][c] for c in range(N)] for r in range(N)]

    cur_tree.clear()
    die_tree.clear()
    new_tree.clear()

print(len(tree_info))
