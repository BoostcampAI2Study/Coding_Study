import sys, collections

N, m, K = map(int, sys.stdin.readline().strip().split())
A = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
TREES = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]
DR = [-1, -1, -1, 0, 0, 1, 1, 1]
DC = [-1, 0, 1, -1, 1, -1, 0, 1]

nourishments = [[5] * N for _ in range(N)]
trees_info = [[collections.deque() for _ in range(N)] for _ in range(N)]
for r, c, tree_age in TREES:
    trees_info[r-1][c-1].append(tree_age)

for k in range(K):
    # spring & summer & winter
    for r in range(N):
        for c in range(N):
            # trees exist
            if trees_info[r][c]:
                nourish_dead_trees = 0

                for _ in range(len(trees_info[r][c])):
                    tree_age = trees_info[r][c].popleft() # get min aged tree

                    if nourishments[r][c] >= tree_age: # spring : nourishing and aging
                        nourishments[r][c] -= tree_age
                        trees_info[r][c].append(tree_age+1)
                    else: # summer : nourishing dead trees
                        nourish_dead_trees += (tree_age // 2)
                        m -= 1
                        
                nourishments[r][c] += nourish_dead_trees

            # winter : supplying nourishments (A)
            nourishments[r][c] += A[r][c]

    # autumn
    for r in range(N):
        for c in range(N):
            # trees exist
            if trees_info[r][c]:
                for tree_age in trees_info[r][c]:
                    if tree_age % 5 == 0:
                        for idx in range(len(DR)):
                            adj_r, adj_c = r+DR[idx], c+DC[idx]
                            
                            if 0 <= adj_r < N and 0 <= adj_c < N: # autumn : breeding
                                trees_info[adj_r][adj_c].appendleft(1)
                                m += 1

print(m)