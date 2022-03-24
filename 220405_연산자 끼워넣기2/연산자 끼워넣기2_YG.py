import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

plus, minus, multiply, divide = map(int, input().split())

answer = []

def dfs(level, value, plus, minus, multiply, divide):
    if level == N-1:
        answer.append(value)
        return

    for idx, operator in enumerate([plus, minus, multiply, divide]):
        if operator > 0:
            if idx == 0:
                dfs(level+1, value+arr[level+1], plus-1, minus, multiply, divide)
            elif idx == 1:
                dfs(level+1, value-arr[level+1], plus, minus-1, multiply, divide)
            elif idx == 2:
                dfs(level+1, value*arr[level+1], plus, minus, multiply-1, divide)
            else:
                if value >= 0:
                    dfs(level+1, value // arr[level+1], plus, minus, multiply, divide-1)
                else:
                    dfs(level+1, -((-value) // arr[level+1]), plus, minus, multiply, divide-1)

dfs(0, arr[0], plus, minus, multiply, divide)

print(max(answer))
print(min(answer))

