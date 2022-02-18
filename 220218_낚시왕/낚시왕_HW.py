import collections
R, C, M = map(int, input().split())
sharks = collections.defaultdict(list)

# shark 정보 저장
for i in range(M):
    shark = list(map(int, input().split()))
    s, d = shark[2], shark[3]
    if d <= 2:
        s = s % (2 * (R - 1))
    if d >= 3:
        s = s % (2 * (C - 1))
    shark[2] = s
    sharks[i + 1] = shark

catch_size = 0
idx_list = list(range(1, M + 1))
reverse_direct = {1: 2, 2: 1, 3: 4, 4: 3}
move_dict = {1: (-1, 0), 2: (1, 0), 3: (0, 1), 4: (0, -1)}

for c in range(C):
    # 상어 잡기
    catch_shark_idx = -1
    catch_shark_r = R + 1
    for idx in idx_list:
        if sharks[idx][1] == c + 1 and sharks[idx][0] < catch_shark_r:
            catch_shark_r = sharks[idx][0]
            catch_shark_idx = idx
    if catch_shark_idx != -1:
        catch_size += sharks[catch_shark_idx][4]
        idx_list.remove(catch_shark_idx)
        del sharks[catch_shark_idx]


    remove_shark = []
    check_size = [[(0, 0)] * (C + 1) for _ in range(R + 1)]
    for idx in idx_list:
        shark_r, shark_c, s, d, z = sharks[idx]
        move = 0
        # 상어 이동
        while move < s:
            nr, nc = move_dict[d][0] + shark_r, move_dict[d][1] + shark_c
            if 0 < nr <= R and 0 < nc <= C:
                move += 1
                shark_r, shark_c = nr, nc
            else:
                d = reverse_direct[d]
        sharks[idx] = [shark_r, shark_c, s, d, z]

        # 중복 위치 상어 확인
        if check_size[shark_r][shark_c][1] < z:
            if check_size[shark_r][shark_c][0] != 0:
                remove_shark.append(check_size[shark_r][shark_c][0])
            check_size[shark_r][shark_c] = (idx, z)
        else:
            remove_shark.append(idx)

    # 중복 위치 상어 제거
    for idx in set(remove_shark):
        del sharks[idx]
        idx_list.remove(idx)

print(catch_size)