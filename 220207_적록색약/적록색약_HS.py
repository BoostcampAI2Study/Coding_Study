from collections import deque
N = int(input())

paint = [input() for _ in range(N)]
# dict for color2int mapping
color_mapping = {'R': 0, 'G': 1, 'B': 2}
# Search for unit areas
def bfs(N, y, x, color):
    global visited
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited[y][x] = 1
    q = deque([(y, x)])
    while q:
        y, x = q.popleft()
        for my, mx in move:
            ny, nx = y+my, x+mx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                if color_mapping[paint[ny][nx]] == color:
                    visited[ny][nx] = 1
                    q.append((ny, nx))

answer = [0, 0]
for i in range(2):
    visited = [[0]*N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                bfs(N, y, x, color_mapping[paint[y][x]])
                answer[i] += 1
    # Red-green blind
    color_mapping['G'] = 0

print(' '.join(map(str, answer)))

# Language        : Python 3
# Memory          : 32420 KB
# Time            : 112 ms
# Time Complexity : O(4N)