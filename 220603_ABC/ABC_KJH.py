# https://www.acmicpc.net/problem/12969


N, K = map(int, input().split())


visited = [
    [[[0] * (N * (N - 1) // 2 + 1) for _ in range(31)] for _ in range(31)]
    for _ in range(N + 2)
]

answer = ""


def dfs(string, A_cnt, B_cnt, k):
    global answer, visited
    if len(string) == N and K == k:
        answer = string
        return True
    if len(string) > N:
        return False
    if visited[len(string)][A_cnt][B_cnt][k]:
        return False
    visited[len(string)][A_cnt][B_cnt][k] = 1
    for s in "ABC":
        if s == "A":
            if dfs(string + s, A_cnt + 1, B_cnt, k):
                return True
        elif s == "B":
            if dfs(string + s, A_cnt, B_cnt + 1, k + A_cnt):
                return True
        elif s == "C":
            if dfs(string + s, A_cnt, B_cnt, k + A_cnt + B_cnt):
                return True
    return False


if dfs("", 0, 0, 0):
    print(answer)
else:
    print("-1")
