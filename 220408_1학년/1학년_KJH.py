# https://www.acmicpc.net/problem/5557

# 중간에 나오는 수가 모두 0이상 20 이하

from collections import defaultdict, deque
import sys

input = sys.stdin.readline

N = int(input())
NUMS = list(map(int, input().split()))
RIGHT_NUM = NUMS[-1]
NUMS = NUMS[:-1]
cnt = 0

dp = [defaultdict(int) for _ in range(N - 1)]
dp[0][NUMS[0]] = 1


def bfs():
    global cnt
    q = deque([(NUMS[0], 1)])
    while q:
        num, i = q.popleft()  # i 이전 까지 연산한 값, idx
        if not 0 <= num <= 20:
            continue
        if i == len(NUMS) - 1:
            if num + NUMS[i] == RIGHT_NUM:
                cnt += dp[i - 1][num]
                dp[i][num + NUMS[i]] += dp[i - 1][num]
            if num - NUMS[i] == RIGHT_NUM:
                cnt += dp[i - 1][num]
                dp[i][num - NUMS[i]] += dp[i - 1][num]
            continue

        if 0 <= num + NUMS[i] <= 20:
            if num + NUMS[i] not in dp[i]:
                q.append((num + NUMS[i], i + 1))

            dp[i][num + NUMS[i]] += dp[i - 1][num]

        if 0 <= num - NUMS[i] <= 20:
            if num - NUMS[i] not in dp[i]:
                q.append((num - NUMS[i], i + 1))
            dp[i][num - NUMS[i]] += dp[i - 1][num]


bfs()
print(cnt)
