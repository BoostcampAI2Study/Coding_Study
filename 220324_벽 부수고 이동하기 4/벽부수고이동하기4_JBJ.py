import collections, sys

N, M = map(int, sys.stdin.readline().rstrip().split())
MAP = [sys.stdin.readline().rstrip() for _ in range(N)]
visited = [[False]*M for _ in range(N)]
vacant_group_map, vacant_group_cnt = [[0]*M for _ in range(N)], collections.defaultdict(int)

# group indexing at vacant places
group_idx = 1
for vacant_y in range(N):
    for vacant_x in range(M):
        if MAP[vacant_y][vacant_x] == '0' and not visited[vacant_y][vacant_x]:
            Q = collections.deque([(vacant_y, vacant_x)])
            visited[vacant_y][vacant_x], total_cnt = True, 1
            while Q:
                y, x = Q.popleft()
                vacant_group_map[y][x] = group_idx
                for new_y, new_x in (y+1, x), (y-1, x), (y, x+1), (y, x-1):
                    if 0 <= new_y < N and 0 <= new_x < M and MAP[new_y][new_x] == '0' and not visited[new_y][new_x]:
                        visited[new_y][new_x] = True
                        total_cnt += 1
                        Q.append((new_y, new_x))
            vacant_group_cnt[group_idx] = total_cnt
            group_idx += 1

# print out possible move count
answer = [[0]*M for _ in range(N)]
for y in range(N):
    for x in range(M):
        total_move_cnt = 0
        if MAP[y][x] == '1':
            total_move_cnt, group_visited = 1, set([0])
            for new_y, new_x in (y+1, x), (y-1, x), (y, x+1), (y, x-1):
                if 0 <= new_y < N and 0 <= new_x < M and vacant_group_map[new_y][new_x] not in group_visited:
                    group_visited.add(vacant_group_map[new_y][new_x])
                    total_move_cnt = (total_move_cnt+vacant_group_cnt[vacant_group_map[new_y][new_x]]) % 10
        answer[y][x] = total_move_cnt

for idx in range(N):
    print(''.join(map(str, answer[idx])))