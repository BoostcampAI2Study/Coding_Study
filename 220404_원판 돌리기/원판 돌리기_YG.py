import sys
input = sys.stdin.readline

N, M, T = map(int, input().split())

wonpan = [list(map(int, input().split())) for _ in range(N)]


for time in range(T):
    # x: 배수 원판 회전, d: 회전 방향(0: 시계, 1: 반시계), k: 회전칸수
    x, d, k = map(int, input().split())

    k %= M

    # 회전
    idx1 = x-1
    while idx1 < N:
        tmp = [-1]*M

        if d == 0:
            for idx2 in range(M):
                next_idx = idx2+k
                if next_idx >= M:
                    next_idx -= M
                tmp[next_idx] = wonpan[idx1][idx2]
        else:
            for idx2 in range(M):
                next_idx = idx2-k
                if next_idx < 0:
                    next_idx += M
                tmp[next_idx] = wonpan[idx1][idx2]

        wonpan[idx1] = tmp
        idx1 += x

    # 인접한거 찾기
    delete_list = set()
    for idx1 in range(N):
        for idx2 in range(M):
            if idx2+1 < M:
                if wonpan[idx1][idx2] != 0 and wonpan[idx1][idx2] == wonpan[idx1][idx2+1]:
                    delete_list.add((idx1, idx2))
            else:
                if wonpan[idx1][idx2] != 0 and wonpan[idx1][idx2] == wonpan[idx1][0]:
                    delete_list.add((idx1, idx2))


            if wonpan[idx1][idx2] != 0 and wonpan[idx1][idx2] == wonpan[idx1][idx2-1]:
                delete_list.add((idx1, idx2))


        for idx2 in range(M):
            if idx1+1 < N:
                if wonpan[idx1][idx2] != 0 and wonpan[idx1][idx2] == wonpan[idx1+1][idx2]:
                    delete_list.add((idx1, idx2))
            if idx1-1 >= 0:
                if wonpan[idx1][idx2] != 0 and wonpan[idx1][idx2] == wonpan[idx1-1][idx2]:
                    delete_list.add((idx1, idx2))

    if delete_list:
        for a, b in delete_list:
            wonpan[a][b] = 0
    else:
        cnt = 0
        summ = 0
        for x in range(N):
            for y in range(M):
                if wonpan[x][y] != 0:
                    cnt += 1
                    summ += wonpan[x][y]

        if cnt == 0:
            continue

        average = summ / cnt

        for x in range(N):
            for y in range(M):
                if wonpan[x][y] == 0:
                    continue
                if wonpan[x][y] > average:
                    wonpan[x][y] -= 1
                elif wonpan[x][y] < average:
                    wonpan[x][y] += 1


print(sum(map(sum, wonpan)))