import sys

N, M, T = map(int, sys.stdin.readline().split())
disk_num = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
rotate_info = [list(map(int, sys.stdin.readline().split())) for _ in range(T)]

for i in range(T):
    x, d, k = rotate_info[i]
    check_remove = [[False] * M for _ in range(N)]
    # 회전
    for j in range(N):
        if (j + 1) % x == 0:
            # 반시계 방향
            if d:
                for _ in range(k):
                    disk_num[j].append(disk_num[j][0])
                    del disk_num[j][0]
            # 반시계 방향
            else:
                for _ in range(k):
                    disk_num[j].insert(0, disk_num[j][M - 1])
                    del disk_num[j][M]

    # 인접하는 수 찾기
    is_check = False
    for r in range(N):
        for c in range(M):
            if disk_num[r][c] == 0:
                continue
            for nr, nc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + nr, c + nc
                if 0 <= nr < N and 0 <= nc < M and disk_num[nr][nc] == disk_num[r][c]:
                    check_remove[r][c] = True
                    check_remove[nr][nc] = True
                    is_check = True
                # nc = -1, nc = M
                if nc == -1 and 0 <= nr < N and disk_num[r][M - 1] == disk_num[r][c]:
                    check_remove[r][c] = True
                    check_remove[nr][M-1] = True
                    is_check = True
                if nc == M and 0 <= nr < N and disk_num[r][0] == disk_num[r][c]:
                    check_remove[r][c] = True
                    check_remove[nr][0] = True
                    is_check = True

    if is_check:
        # 제거
        for r in range(N):
            for c in range(M):
                if check_remove[r][c]:
                    disk_num[r][c] = 0
    else:
        # 인접하는 수 없는 
        disk_sum, zero_cnt = 0, 0
        for r in range(N):
            disk_sum += sum(disk_num[r])
            zero_cnt += disk_num[r].count(0)
        if zero_cnt == N * M:
            break
        disk_avg = disk_sum / (N * M - zero_cnt)
        for r in range(N):
            for c in range(M):
                if disk_num[r][c] > disk_avg:
                    disk_num[r][c] -= 1
                elif 0 < disk_num[r][c] < disk_avg:
                    disk_num[r][c] += 1

print(sum(map(sum, disk_num)))
