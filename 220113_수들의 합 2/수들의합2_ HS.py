n, m = map(int, input().split())

arr = list(map(int, input().split()))

answer = 0
start, end = 0, 0
s = arr[start]
while start < len(arr)-1:
    if s < m:
        end += 1
        if end < len(arr):
            s += arr[end]
        else:
            break
    elif s > m:
        if start == end:
            start += 1
            end += 1
            s = arr[start]
        else:
            s -= arr[start]
            start += 1
    else:
        answer += 1
        s -= arr[start]
        start += 1
if arr[-1] == m:
    answer += 1

print(answer)