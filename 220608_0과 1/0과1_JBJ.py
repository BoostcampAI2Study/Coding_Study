"""
(A + B) % MOD = ( (A % MOD) + (B % MOD) ) % MOD
(A * B) % MOD = ( (A % MOD) * (B % MOD) ) % MOD
(A - B) % MOD = ( (A % MOD) - (B % MOD) ) % MOD
"""
import collections, sys
T = int(sys.stdin.readline())

def bfs(n):
    visited, Q = [False]*20001, collections.deque([(1, '1')])
    visited[1] = True
    next_remainders, next_numbers = [-1, -1], ['', '']

    while Q:
        cur_remainder, cur_number = Q.popleft()

        if cur_remainder == 0: # cur_number is the multiple of n.
            return cur_number

        for digit in range(2):
            next_remainders[digit] = ((cur_remainder * 10) + digit) % n
            next_numbers[digit] = cur_number + str(digit)

            if visited[next_remainders[digit]]: continue
            visited[next_remainders[digit]] = True
            Q.append((next_remainders[digit], next_numbers[digit]))
    return 'BRAK'

for _ in range(T):
    N = sys.stdin.readline()
    if set(N) | set(['1', '0']) == set(['1', '0']): print(N)
    else: print(bfs(int(N)))
