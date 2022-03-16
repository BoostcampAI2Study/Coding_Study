from sys import stdin

input = stdin.readline

n = int(input())    # 수열 크기
nums = list(map(int, input().split()))  # 수열
m = int(input())    # 홍준이 질문 수
question = [list(map(int, input().split())) for _ in range(m)]  # 홍준이 질문


# 팰린드롬을 먼저 구하기
pal = [[0] * n for _ in range(n)]

# 중심 팰린드롬
for i in range(n):
    # 길이 1인 팰린드롬
    pal[i][i] = 1

    if i == n-1:
        break

    # 길이 2인 팰린드롬
    if nums[i] == nums[i+1]:
        pal[i][i+1] = 1


# 팰린드롬 체크
for num_len in range(n):
    for l in range(n - num_len):
        r = l + num_len
        if l == r:
            continue
        
        if nums[l] == nums[r] and pal[l+1][r-1] == 1:
            pal[l][r] = 1


for s, e in question:
    print(pal[s-1][e-1])
