from sys import stdin
from collections import Counter

input = stdin.readline
word_count = int(input())
word_dict = {}

words = []
priority = Counter()
max_len = 0

for _ in range(word_count):
    words.append(input().strip())
    priority += Counter(words[-1])
    max_len = max(max_len, len(words[-1]))

words = list(map(lambda x: x.rjust(max_len), words))
digit = 9
answer = 0

for i, alphas in enumerate(zip(*words)):
    _sum = 0
    
    for alpha in sorted(alphas, key=lambda x: priority[x], reverse=True):
        if alpha == ' ':
            continue
        
        if not word_dict.get(alpha):
            word_dict[alpha] = digit
            digit -= 1
        
        _sum += word_dict[alpha]

    answer += _sum * (10 ** (max_len - i - 1))

print(answer)