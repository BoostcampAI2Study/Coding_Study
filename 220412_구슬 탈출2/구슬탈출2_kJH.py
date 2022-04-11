# https://www.acmicpc.net/problem/13460

from collections import defaultdict, deque


def solution():
    N, M = map(int, input().split())
    table = []
    hole = R_pos = B_pos = None
    for i in range(N):
        tmp = list(input())
        if B_pos is None and "B" in tmp:
            B_pos = [i, tmp.index("B")]
        if R_pos is None and "R" in tmp:
            R_pos = [i, tmp.index("R")]
        if hole is None and "O" in tmp:
            hole = [i, tmp.index("O")]
        table.append(tmp)

    min_cnt = 12

    dir = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

    def bfs(cur_inclination, cnt, R_pos, B_pos):
        nonlocal min_cnt
        q = deque([[cur_inclination, cnt, R_pos, B_pos]])
        while q:
            cur_inclination, cnt, R_pos, B_pos = q.popleft()
            if cnt == 11:
                return

            prev_R_pos = R_pos[:]
            prev_B_pos = B_pos[:]
            r_hole = False
            b_hole = False
            red_stop = blue_stop = False
            while not red_stop or not blue_stop:
                red_stop = blue_stop = False
                # 빨간거 이동
                if not r_hole:
                    if table[R_pos[0] + dir[cur_inclination][0]][
                        R_pos[1] + dir[cur_inclination][1]
                    ] == "#" or (
                        R_pos[0] + dir[cur_inclination][0] == B_pos[0]
                        and R_pos[1] + dir[cur_inclination][1] == B_pos[1]
                    ):
                        red_stop = True
                    else:
                        R_pos[0] = R_pos[0] + dir[cur_inclination][0]
                        R_pos[1] = R_pos[1] + dir[cur_inclination][1]
                        if R_pos == hole:
                            r_hole = True
                            red_stop = True
                else:
                    red_stop = True

                # 파란거 이동
                if not b_hole:
                    if table[B_pos[0] + dir[cur_inclination][0]][
                        B_pos[1] + dir[cur_inclination][1]
                    ] == "#" or (
                        not r_hole
                        and B_pos[0] + dir[cur_inclination][0] == R_pos[0]
                        and B_pos[1] + dir[cur_inclination][1] == R_pos[1]
                    ):
                        blue_stop = True
                    else:
                        B_pos[0] = B_pos[0] + dir[cur_inclination][0]
                        B_pos[1] = B_pos[1] + dir[cur_inclination][1]
                        if B_pos == hole:
                            b_hole = True
                            blue_stop = True
                else:
                    blue_stop = True
            if prev_B_pos == B_pos and prev_R_pos == R_pos:
                continue
            if r_hole:
                if not b_hole:
                    min_cnt = min(min_cnt, cnt)
                    return

            if not r_hole and not b_hole:
                if B_pos not in red_blue_pos_pair[tuple(R_pos)]:
                    red_blue_pos_pair[tuple(R_pos)].append(B_pos)
                    for direct in ["R", "L", "U", "D"]:
                        q.append([direct, cnt + 1, R_pos[:], B_pos[:]])

    red_blue_pos_pair = defaultdict(list)
    bfs("U", 1, R_pos[:], B_pos[:])
    red_blue_pos_pair = defaultdict(list)
    bfs("D", 1, R_pos[:], B_pos[:])
    red_blue_pos_pair = defaultdict(list)
    bfs("L", 1, R_pos[:], B_pos[:])
    red_blue_pos_pair = defaultdict(list)
    bfs("R", 1, R_pos[:], B_pos[:])

    if min_cnt == 12:
        return -1
    return min_cnt


print(solution())

