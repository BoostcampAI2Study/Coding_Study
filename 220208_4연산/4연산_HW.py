import collections
import sys

s, t = map(int, input().split())

if s == t:
    print(0)
    sys.exit()

result = []
visit = collections.defaultdict(int)
q = collections.deque()
q.append((s, ""))
while q:
    num, seq = q.popleft()
    if num == t:
        result.append(seq)
        break
    visit[num] = 1

    if abs(num * num) <= abs(t):
        if visit[abs(num * num)] != 1:
            q.append((num * num, seq + "*"))
    if abs(num + num) <= abs(t):
        if visit[abs(num + num)] != 1:
            q.append((num + num, seq + "+"))
    if visit[0] != 1:
        q.append((0, seq + "-"))
    if num != 0:
        if visit[1] != 1:
            q.append((1, seq + "/"))
if result:
    print(result[0])
else:
    print(-1)