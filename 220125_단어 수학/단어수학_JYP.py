import heapq
from collections import deque, defaultdict

# first trial => fail
n = int(input())
d = dict()
texts = []
tmps = []
for _ in range(n):
    text = input()
    tmps.append(text)
    heapq.heappush(texts, (-len(text), deque(list(text))))

value = 9
while value >= 0:
    if texts[0][0] == 0:
        break
    l, q = heapq.heappop(texts)
    c = q.popleft()
    if not d.get(c):
        d[c] = value
        value -= 1
    l += 1
    heapq.heappush(texts, (l, q))

nums = []
for tmp in tmps:
    s = ''
    for c in tmp:
        s += str(d[c])
    nums.append(int(s))

print(sum(nums))


# second trial => success
dd = defaultdict(int)
texts = []
for _ in range(n):
    texts.append(input())

for text in texts:
    l = len(text) - 1
    for c in text:
        dd[c] += 10 ** l
        l -= 1

values = sorted(dd.values(), reverse=True)
ans = 0
digit = 9
for value in values:
    ans += value * digit
    digit -= 1

print(ans)

# 2
# AB
# BA
