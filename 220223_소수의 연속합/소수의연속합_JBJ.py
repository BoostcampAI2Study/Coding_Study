def eratosthenes():
    global N
    is_prime = [False, False] + [True]*(N-1)
    
    square_root_of_N = N**0.5
    for n in range(2, int(square_root_of_N)+1):
        if is_prime[n]:
            for multiples in range(n*2, N+1, n):
                is_prime[multiples] = False
    
    return [n for n, prime in enumerate(is_prime) if prime]

N = int(input())
prime_numbers = eratosthenes() 
left_ptr, right_ptr, n_cnt = 0, 0, 0

if prime_numbers:
    cur_sum = prime_numbers[0]
    while left_ptr <= right_ptr < len(prime_numbers):
        if N >= cur_sum: # right pointer move
            if cur_sum == N: n_cnt += 1
            right_ptr += 1
            if right_ptr == len(prime_numbers): break
            cur_sum += prime_numbers[right_ptr]
        else: # left pointer move
            cur_sum -= prime_numbers[left_ptr]
            left_ptr += 1

print(n_cnt)