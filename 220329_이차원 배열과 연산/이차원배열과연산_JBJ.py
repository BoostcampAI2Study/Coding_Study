import collections, sys

R, C, K = map(int, input().rstrip().split())
A = [list(map(int, input().rstrip().split())) for _ in range(3)]
time = 0

def operation(is_row=True):
    global A, col_len, row_len

    # number of appearances count
    max_len = 0
    for idx in range(len(A)):
        num_counts, temp_a = collections.Counter(A[idx]), []
        del num_counts[0]
        num_counts = list(num_counts.items())
        num_counts.sort(key=lambda x:(x[1], x[0]))
        for num, appear_cnt in num_counts[:50]:
            temp_a.extend([num, appear_cnt])
        A[idx] = temp_a
        max_len = max(max_len, len(A[idx]))
    # zero-padding
    for idx in range(len(A)):
        if len(A[idx]) < max_len:
            A[idx].extend([0]*(max_len - len(A[idx])))

while time <= 100:
    if R-1 < len(A) and C-1 < len(A[0]) and A[R-1][C-1] == K: 
        print(time)
        sys.exit()

    if len(A) >= len(A[0]):
        operation()
    else:
        A = list(map(list, zip(*A))) # transpose
        operation(is_row=False)
        A = list(map(list, zip(*A))) # transpose
    time += 1  
print(-1)