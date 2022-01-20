N, K = map(int, input().split())

graph = [[[] for _ in range(N)] for _ in range(N)]
colormap = []
for _ in range(N):
    colormap.append(list(map(int, input().split())))

direction = {} # 체스말 번호 별 방향
location = {} # 체스말 위치
for i in range(K):
    r, c, d = map(int, input().split())
    #   3
    # 2   1
    #   4
    location[i+1] = (r-1, c-1)
    graph[r-1][c-1].append(i+1)
    direction[i+1] = d

def finished(graph):
    for r in graph:
        for c in r:
            if len(c) >= 4:
                return True
    return False


def next(r, c, num):
    # num = graph[r][c][0]
    if direction[num] == 1:
        nr, nc = r, c+1
    elif direction[num] == 2:
        nr, nc = r, c-1
    elif direction[num] == 3:
        nr, nc = r-1, c
    elif direction[num] == 4:
        nr, nc = r+1, c

    if 0<=nr<N and 0<=nc<N:
        return nr, nc
    else:
        return -1, -1


def move_white_red(nr, nc, r, c, num):
    num_idx = graph[r][c].index(num)
    # 흰색
    if colormap[nr][nc] == 0:
        graph[nr][nc].extend(graph[r][c][num_idx:]) # 쌓기
        graph[r][c] = graph[r][c][:num_idx]
        for n in graph[nr][nc]:
            location[n] = (nr, nc)
    
    # 빨강
    elif colormap[nr][nc] == 1:
        graph[nr][nc].extend(reversed(graph[r][c][num_idx:])) # 뒤집어서 쌓기
        graph[r][c] = graph[r][c][:num_idx]
        for n in graph[nr][nc]:
            location[n] = (nr, nc)


def main():
    turn = 0
    flag = 0
    while not finished(graph):
        turn += 1
        # print(graph)

        if turn > 1000:
            break

        for num in range(1, K+1):
            # 4개이상 시 즉시 탈출
            if finished(graph):
                break
            r, c = location[num]

            # # 해당 번호의 말이 가장 아래있지 않은 경우 continue
            # if graph[r][c][0] != num:
            #     continue
            
            nr, nc = next(r, c, num) # 이동할 좌표 (그래프를 벗어날 경우 -1, -1)

            # 다음칸이 파랑 or 그래프 밖
            if (nr, nc) == (-1, -1) or colormap[nr][nc] == 2:
                # 방향 반대로
                if direction[num] % 2 == 0:
                    direction[num] -= 1
                elif direction[num] % 2 == 1:
                    direction[num] += 1

                nr, nc = next(r, c, num)
                # 반대방향이 그래프 범위 내 인 경우
                if (nr, nc) != (-1, -1):
                    move_white_red(nr, nc, r, c, num)
            
            else:
                move_white_red(nr, nc, r, c, num)
            
    if turn>1000:
        print(-1)
    else:
        print(turn)

main()
