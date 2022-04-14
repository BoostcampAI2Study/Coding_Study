import collections, itertools

T = int(input().rstrip())
LEN_A, LIST_A = int(input().rstrip()), list(map(int, input().rstrip().split()))
LEN_B, LIST_B = int(input().rstrip()), list(map(int, input().rstrip().split()))
a_sub_sums = collections.defaultdict(int) # {sub_list_sum: # of cases}

a_cumulative_sums, b_cumulative_sums = [0, LIST_A[0]], [0, LIST_B[0]]
for idx in range(1, LEN_A):
    a_cumulative_sums.append(a_cumulative_sums[-1] + LIST_A[idx])
for idx in range(1, LEN_B):
    b_cumulative_sums.append(b_cumulative_sums[-1] + LIST_B[idx])

for delete_idx in range(LEN_A): # cumulatives: {1, 1+3, 1+3+1, 1+3+1+2}, e.g. delete {1}.
    for remain_idx in range(delete_idx+1, LEN_A+1): # cumulatives: {1, 1+3, 1+3+1, 1+3+1+2}, e.g. remain {1+3, ...}.
        sub_list_sum = a_cumulative_sums[remain_idx] - a_cumulative_sums[delete_idx]
        a_sub_sums[sub_list_sum] += 1

t_pair_cnt = 0
for delete_idx in range(LEN_B):
    for remain_idx in range(delete_idx+1, LEN_B+1):
        sub_list_sum = b_cumulative_sums[remain_idx] - b_cumulative_sums[delete_idx]
        if T - sub_list_sum in a_sub_sums:
            t_pair_cnt += a_sub_sums[(T - sub_list_sum)]

print(t_pair_cnt)