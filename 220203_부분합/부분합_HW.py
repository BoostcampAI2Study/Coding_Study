N, S = map(int, input().split())
seq_list = list(map(int, input().split()))

left, right = 0, 0
result = 1e6
cur_sum = seq_list[0]
while right < N:
    if cur_sum >= S:
        min_seq = right - left + 1
        if result > min_seq:
            result = min_seq
        cur_sum -= seq_list[left]
        left += 1
    else:
        right += 1
        if right < N:
            cur_sum += seq_list[right]

print(result) if result != 1e6 else print(0)