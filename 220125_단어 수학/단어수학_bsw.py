N = int(input())
alphas = []

for _ in range(N):
    alphas.append(input())


'''
10000a 1010c 100d 10e 1b 100g 1f
'''

from collections import defaultdict
d=defaultdict(int)

for alpha in alphas:
    for i, v in enumerate(alpha):
        d[v] += 10**(len(alpha)-i -1)
        
num=9
answer = 0
for k in sorted(d, key=lambda x : -d[x]):
    answer += d[k]*num
    num -= 1

print(answer)
