from collections import deque, defaultdict

N = int(input())
answer = 0
words = []
nums = deque([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
word_num = defaultdict(int)

for i in range(N):
    tmp = input()
    for j in range(1, len(tmp)+1):
        word_num[tmp[-j]] += 10**(j-1)

for v in sorted(word_num.values(), reverse=True):
    answer += v * nums.popleft()

print(answer)