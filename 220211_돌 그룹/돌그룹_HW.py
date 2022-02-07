import collections
import sys

stones = list(map(int, input().split()))

# 동일 분배 완전히 불가한 경우
goal_num = sum(stones) // 3
if goal_num * 3 != sum(stones):
    print(0)
    exit(0)

visit = [[False] * 1500 for _ in range(1500)]
q = collections.deque()
q.append(stones)

while q:
    a, b, c = q.popleft()
    if a == b == c:
        print(1)
        sys.exit()
    if a < b and visit[2 * a][b - a] is False:
        q.append([2 * a, b - a, c])
        visit[2 * a][b - a] = True
    elif b < a and visit[a - b][2 * b] is False:
        q.append([a - b, 2 * b, c])
        visit[a - b][2 * b] = True
    if b < c and visit[2 * b][c - b] is False:
        q.append([a, 2 * b, c - b])
        visit[2 * b][c - b] = True
    elif b > c and visit[b - c][2 * c] is False:
        q.append([a, b - c, 2 * c])
        visit[b - c][2 * c] = True
    if a < c and visit[2 * a][c - a] is False:
        q.append([2 * a, b, c - a])
        visit[2 * a][c - a] = True
    elif a > c and visit[a - c][2 * c] is False:
        q.append([a - c, b, 2 * c])
        visit[a - c][2 * c] = True

print(0)
