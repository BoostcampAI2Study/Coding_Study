import re

def solution(n, k):

    def get_notation(n, k):
        if k == 10: return str(n)

        rev_notation = ''
        while n > 0:
            n, mod = divmod(n, k)
            rev_notation += str(mod)

        return rev_notation[::-1]

    def is_prime(n):
        for denominator in range(2, int(n**0.5)+1):
            if n % denominator == 0: return False

        return True

    n, answer = get_notation(n, k), 0
    for prime_candidate in map(lambda x: int(x) if x != '' else -1, re.split('0+', n)):
        if prime_candidate > 1 and is_prime(prime_candidate): answer += 1

    return answer
