M, N = map(int, input().split())

m, n, cur_num = (M-2), (N-2), 1+(N-1)+(M-1)+(N-1)
turn_cnt = 3 if cur_num < (M*N) else 2 # 1+(N-1), 1+(N-1)+(M-1), 1+(N-1)+(M-1)+(N-1) => corner numbers
m_flag = 1
while True:
    cur_num += m if m_flag else n

    if cur_num < (M*N): turn_cnt += 1
    else: break

    if m_flag: m -= 1
    else: n -= 1

    m_flag = 1-m_flag

print(turn_cnt)