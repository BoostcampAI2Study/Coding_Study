from collections import deque, defaultdict
import sys

def _input():
    return list(map(int, input().split()))

s, t = _input()
# Exception
if s == t:
    print(0)
    sys.exit()
# Memoization
visited = defaultdict(int)
visited[s] = 1

q = deque([(s, '')])
answer = []
# Using BFS
while q:
    number, oper = q.popleft()
    if number == t:
        answer.append(oper)
    if not visited[number**2] and number**2 <= t:
        visited[number**2] = 1
        q.append((number**2, oper + '*'))
    if not visited[number*2] and number*2 <= t:
        visited[number*2] = 1
        q.append((number*2, oper + '+'))
    if not visited[0]:
        visited[0] = 1
        q.append((0, oper + '-'))
    if number != 0 and not visited[1]:
        visited[1] = 1
        q.append((1, oper + '/'))
    
if answer:
    print(min(answer))
else:
    print(-1)


# Language        : Python3
# Memory          : 32404 KB
# Time            : 100ms
# Time Complexity : O(t/s) maximum 10^9