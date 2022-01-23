import collections

def bfs(start_r, start_c, h, w, test_map):
    visited = [[-1] * (w + 2) for _ in range(h + 2)]
    q = collections.deque()
    q.append((start_r, start_c))
    visited[start_r][start_c] = 0

    while q:
        r, c = q.popleft()

        for nr, nc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            nr, nc = nr + r, nc + c
            if nr < 0 or nr > h + 1 or nc < 0 or nc > w + 1 or test_map[nr][nc] == "*" or visited[nr][nc] != -1:
                continue
            if test_map[nr][nc] == "." or test_map[nr][nc] == "$":
                q.appendleft((nr, nc))
                visited[nr][nc] = visited[r][c]
            elif test_map[nr][nc] == "#":
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
    return visited

input_list = []
K = int(input())
for _ in range(K):
    h, w = map(int, input().split())
    prison_map = [list('.' + input() + '.') for _ in range(h)]
    prison_map.insert(0, ['.'] * (w + 2))
    prison_map.append(['.'] * (w + 2))
    input_list.append([h, w, prison_map])

for h, w, test_map in input_list:
    # 죄수 위치 찾기
    prisoners, exits = [], []
    for r in range(h):
        for c in range(w):
            if test_map[r][c] == "$":
                prisoners.append((r, c))

    # 죄수와 외부에서 bfs 실행
    door_maps = []
    for loc_prisoner in prisoners:
        door_maps.append(bfs(loc_prisoner[0], loc_prisoner[1], h, w, test_map))
    door_maps.append(bfs(0, 0, h, w, test_map))

    # bfs 결과 최소 문 찾기
    door_cnt = 1e9
    for r in range(h + 2):
        for c in range(w + 2):
            if test_map[r][c] == "*":
                continue
            tmp = 0
            for door_map in door_maps:
                tmp += door_map[r][c]
            if test_map[r][c] == "#":
                tmp -= 2
            if tmp < 0:
                continue
            door_cnt = min(door_cnt, tmp)

    print(door_cnt)