n, m = map(int, input().split())
A = [int(k) for k in input().split()]

left, right, cnt = 0, 1, 0
while left <= len(A) and right <= len(A):
    if sum(A[left:right]) < m:
        right += 1
    elif sum(A[left:right]) > m:
        left += 1
    else:
        right += 1
        cnt += 1
print(cnt)
