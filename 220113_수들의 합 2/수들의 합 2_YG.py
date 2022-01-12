n, m = map(int, input().split())

arr = list(map(int, input().split()))

start = 0
end = 0

ans = 0

sum_arr = arr[start]

while 1:
    if sum_arr == m:
        ans += 1
        end += 1
        start += 1
        if end < n:
            sum_arr -= arr[start-1]
            sum_arr += arr[end]

    elif sum_arr < m:
        end += 1
        if end < n:
            sum_arr += arr[end]
    else:
        start += 1
        sum_arr -= arr[start-1]

    if end == n:
        break

print(ans)
