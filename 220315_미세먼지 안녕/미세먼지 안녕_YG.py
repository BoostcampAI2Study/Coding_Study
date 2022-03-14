import sys

input = sys.stdin.readline

R, C, T = map(int, input().split())

# 입력받기
machine = []
graph = []
for x in range(R):
    sub = list(map(int, input().split()))
    for y in range(C):
        if sub[y] == -1:
            machine.append((x, y))
    graph.append(sub)

# 방향 설정
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# T초만큼 실행
for _ in range(T):
    n_graph = [[0]*C for _ in range(R)]
    # 미세먼지 확산
    for x in range(R):
        for y in range(C):
            # 청정기가 아니고 먼지가 있다면
            if graph[x][y] > 0:
                diffusion_value = graph[x][y] // 5
                diffusion_sum = 0
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != -1:
                        n_graph[nx][ny] += diffusion_value
                        diffusion_sum += diffusion_value
                n_graph[x][y] += (graph[x][y] - diffusion_sum)
    graph = n_graph

    # 공기청정기 작동
    nn_graph = [[0]*C for _ in range(R)]
    # 위쪽 (반시계 방향)
    m_x, m_y = machine[0][0], machine[0][1]
    s_x, s_y = 0, 0
    t_x, t_y = m_x, C-1
    # 1번(왼쪽)
    for idx in range(1, C):
        nn_graph[0][idx-1] = graph[0][idx]
    # 2번(아래로)
    for idx in range(t_x):
        nn_graph[idx+1][0] = graph[idx][0]
    # 3번(오른쪽)
    for idx in range(C-1):
        nn_graph[t_x][idx+1] = graph[t_x][idx]
    # 4번(위쪽)
    for idx in range(1, t_x+1):
        nn_graph[idx-1][t_y] = graph[idx][t_y]

    # 아래쪽 (시계 방향)
    m_x, m_y = machine[1][0], machine[1][1]
    s_x, s_y = m_x, m_y
    t_x, t_y = R-1, C-1

    # 1번(오른쪽)
    for idx in range(C-1):
        nn_graph[s_x][idx+1] = graph[s_x][idx]
    # 2번(아래로)
    for idx in range(s_x,t_x):
        nn_graph[idx+1][t_y] = graph[idx][t_y]
    # 3번(왼쪽)
    for idx in range(1, C):
        nn_graph[t_x][idx-1] = graph[t_x][idx]
    # 4번(위쪽)
    for idx in range(s_x+1, t_x+1):
        nn_graph[idx-1][0] = graph[idx][0]

    for x in range(R):
        for y in range(C):
            if x == 0 or x == R-1 or y == 0 or y == C-1 or x == machine[0][0] or x == machine[1][0]:
                pass
            else:
                nn_graph[x][y] += graph[x][y]

    graph = nn_graph
    # 공기청정기 넣어주기
    for a, b in machine:
        graph[a][b] = -1


# 정답 출력
print(sum(map(sum, graph))+2)




