from collections import deque
import heapq as hq
from collections import deque, Counter, defaultdict

N = int(input())
answer = 0
words = []
nums = deque([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
word_dict = dict()
word_num = defaultdict(list)

for i in range(N):
    tmp = input()
    for j in range(1, len(tmp)+1):
        word_num[j].append(tmp[-j])

for k, v in sorted(word_num.items(), reverse=True):
    counter = Counter(v).most_common()
    for c, n in counter:
        if c not in word_dict:
            word_dict[c] = nums.popleft()
        answer += 10**(k-1) * word_dict[c] * n

print(answer)