n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt, left, right = 0, 0, 1

while left <= right:
    total = sum(a[left:right])
    if total == m:
        cnt += 1
        left += 1
    elif total > m:
        left += 1
    else:
        if right + 1 <= n:
            right += 1
        else:
            break
print(cnt)
