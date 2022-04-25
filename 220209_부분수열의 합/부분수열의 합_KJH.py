# https://www.acmicpc.net/problem/1182


N, S = map(int, input().split())
NUMS = list(map(int, input().split()))
NUMS.sort()
answer = 0
print(NUMS)


def dfs(idx, total):
    global answer
    if total == S:
        answer += 1
    for i in range(idx + 1, N):
        dfs(i, total + NUMS[i])

for i in range(N):
    dfs(i, NUMS[i])

print(answer)
