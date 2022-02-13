from itertools import combinations

N, S = list(map(int, input().split()))
arr = list(map(int, input().split()))

answer = 0
# Exploring all cases
for i in range(N):
    for sub in combinations(arr, i+1):
        if sum(sub) == S:
            answer += 1

print(answer)

# Language        : Python3
# Memory          : 30864 KB
# Time            : 420 ms
# Time complexity : O(N^(N/2))