import collections, sys
T = int(sys.stdin.readline().rstrip())

# Sieve of Eratosthenes
SIEVE = [False, False] + ([True] * (9999-1)) 
for num in range(2, int(9999**0.5)+1):
    if SIEVE[num] == True:
        for next_num in range(num*2, 10000, num):
            SIEVE[next_num] = False

def bfs():
    global FROM_PRIME, SIEVE, TO_PRIME

    visited = [False]*10000
    visited[int(FROM_PRIME)] = True
    Q = collections.deque()
    Q.append((FROM_PRIME, 0))
    while Q:
        prime, convertion_cnt = Q.popleft()

        for digit in range(4): 
            for num in range(0 if digit else 1, 10):
                if prime[digit] != num: # The number must be different to convert.
                    new_prime = prime[:digit] + str(num) + prime[digit+1:]
                    if not visited[int(new_prime)] and SIEVE[int(new_prime)]: # visited & prime check.
                        if new_prime == TO_PRIME:
                            return convertion_cnt+1
                        visited[int(new_prime)] = True
                        Q.append((new_prime, convertion_cnt+1))
    return 'Impossible'

for _ in range(T):
    FROM_PRIME, TO_PRIME = sys.stdin.readline().rstrip().split()
    print(bfs() if FROM_PRIME != TO_PRIME else 0)