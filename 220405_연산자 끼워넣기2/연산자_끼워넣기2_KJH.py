# https://www.acmicpc.net/problem/15658

N = int(input())
A = list(map(int, input().split()))
operators = list(map(int, input().split()))

min_answer = float("inf")
max_answer = -float("inf")


def dfs(answer, idx):
    global min_answer, max_answer
    if idx == len(A):
        min_answer = min(min_answer, answer)
        max_answer = max(max_answer, answer)
        return
    for i in range(len(operators)):
        if operators[i] == 0:
            continue
        operators[i] -= 1
        if i == 0:
            dfs(answer + A[idx], idx + 1)
        elif i == 1:
            dfs(answer - A[idx], idx + 1)
        elif i == 2:
            dfs(answer * A[idx], idx + 1)
        else:
            dfs(answer // A[idx], idx + 1) if answer >= 0 else dfs(
                -((-answer) // A[idx]), idx + 1
            )
        operators[i] += 1


dfs(A[0], 1)
print(max_answer)
print(min_answer)
