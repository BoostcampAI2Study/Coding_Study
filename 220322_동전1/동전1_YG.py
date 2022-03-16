# n = 동전의 종류, k = 가치의 합
n, k = map(int ,input().split())

# dp 테이블 생성
dp = [0] * (10001)
dp[0] = 1

# 동전 입력받기
coins = []
for _ in range(n):
    coins.append(int(input()))

# dp 테이블 업데이트
for coin in coins:
    for i in range(1, k + 1):
        if i - coin >= 0:
            dp[i] += dp[i-coin]

print(dp[k])