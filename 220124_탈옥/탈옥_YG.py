# reference: https://rebas.kr/770

from collections import deque, defaultdict
import sys

input = sys.stdin.readline

T = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 테스트 케이스만큼 for문 진행
for _ in range(T):
    h, w = map(int, input().split())
    bfs_list = [(0,0)]
    prison = [["."]*(w+2)]
    check_list = []

    for _ in range(h):
        prison.append(list('.'+input().strip()+'.'))
    prison.append(["."]*(w+2))

    for a in range(h+2):
        for b in range(w+2):
            if prison[a][b] == '$':
                bfs_list.append((a,b))
            elif prison[a][b] == '#':
                check_list.append((a,b))

    answer = [[0]*(w+2) for _ in range(h+2)]
    for x, y in bfs_list:
        visited = [[1e9]*(w+2) for _ in range(h+2)]
        visited[x][y] = 0

        q = deque()

        q.append((x, y))

        while q:
            x, y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < h+2 and 0 <= ny < w+2 and visited[nx][ny] == 1e9:
                    if prison[nx][ny] == '.' or prison[nx][ny] == '$':
                        visited[nx][ny] = visited[x][y]
                        q.appendleft((nx, ny))
                    elif prison[nx][ny] == '#':
                        visited[nx][ny] = visited[x][y]+1
                        q.append((nx, ny))

        for a in range(h+2):
            for b in range(w+2):
                answer[a][b] += visited[a][b]

    for a, b in check_list:
        answer[a][b] -= 2

    print(min(map(min, answer)))


