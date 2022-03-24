import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    K = int(sys.stdin.readline().rstrip())
    COSTS = list(map(int, sys.stdin.readline().rstrip().split()))
    files = [[0]*(K) for _ in range(K)]
    # total sum between start and end indices
    for start_idx in range(K-1):
        files[start_idx][start_idx+1] = COSTS[start_idx] + COSTS[start_idx+1] # 2 files
        for end_idx in range(start_idx+2, K):
            files[start_idx][end_idx] = files[start_idx][end_idx-1] + COSTS[end_idx] # 3+ files

    # minimum(start:mid, mid+1:end)
    for distance in range(2, K):
        for start_idx in range(K-distance):
            end_idx = start_idx + distance
            sum_list = [files[start_idx][mid] + files[mid+1][end_idx] for mid in range(start_idx, end_idx)]
            files[start_idx][end_idx] += min(sum_list)

    print(files[0][-1])