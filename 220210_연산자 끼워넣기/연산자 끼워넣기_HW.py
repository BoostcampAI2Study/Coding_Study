import collections

N = int(input())
A = list(map(int, input().split()))
op_cnt = list(map(int, input().split()))

q = collections.deque()
q.append((A[0], 0, op_cnt))
max_res = -1e9
min_res = 1e9

while q:
    num, idx, op_cnt = q.popleft()
    if idx == N - 1:
        if max_res < num:
            max_res = num
        if min_res > num:
            min_res = num
    for op, cnt in enumerate(op_cnt):
        tmp_cnt = op_cnt[:]
        if cnt == 0:
            continue
        tmp_cnt[op] -= 1
        if op == 0:
            q.append((num + A[idx + 1], idx + 1, tmp_cnt))
        elif op == 1:
            q.append((num - A[idx + 1], idx + 1, tmp_cnt))
        elif op == 2:
            q.append((num * A[idx + 1], idx + 1, tmp_cnt))
        elif op == 3:
            if num < 0:
                q.append((-(abs(num) // A[idx + 1]), idx + 1, tmp_cnt))
            else:
                q.append((num // A[idx + 1], idx + 1, tmp_cnt))

print(max_res, min_res)