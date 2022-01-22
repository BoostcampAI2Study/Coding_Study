# reference: https://derooty.tistory.com/53
import sys
from itertools import combinations
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

dx = [0,1]
dy = [1,0]

P_NUM = 1
while 1:

    N = int(input())
    if N == 0:
        break

    print('Puzzle '+ str(P_NUM))

    puzzle = [[0]*9 for _ in range(9)]
    check_dominos = [[False]*10 for _ in range(10)]

    # 스도쿠 체크
    is_sdoku_1 = [[False]*10 for _ in range(9)]
    is_sdoku_2 = [[False]*10 for _ in range(9)]
    is_sdoku_3 = [[False]*10 for _ in range(9)]


    for _ in range(N):

        U, LU, V, LV = input().split()
        U_X, U_Y = ord(LU[0])-ord('A'), int(LU[1])-1
        V_X, V_Y = ord(LV[0])-ord('A'), int(LV[1])-1

        puzzle[U_X][U_Y] = int(U)
        puzzle[V_X][V_Y] = int(V)
        is_sdoku_1[U_X][int(U)], is_sdoku_1[V_X][int(V)] = True, True
        is_sdoku_2[U_Y][int(U)], is_sdoku_2[V_Y][int(V)] = True, True
        is_sdoku_3[(U_X//3)*3 + (U_Y//3)][int(U)], is_sdoku_3[(V_X//3)*3 + (V_Y//3)][int(V)] = True, True
        check_dominos[int(V)][int(U)], check_dominos[int(U)][int(V)] = True, True


    filled_number = list(input().split())

    for idx, address in enumerate(filled_number):
        AX, AY = ord(address[0])-ord('A'), int(address[1])-1
        puzzle[AX][AY] = idx+1
        is_sdoku_1[AX][idx+1] = True
        is_sdoku_2[AY][idx+1] = True
        is_sdoku_3[(AX//3)*3 + (AY//3)][idx+1] = True

    remain = []

    for a in range(9):
        for b in range(9):
            if puzzle[a][b] == 0:
                remain.append((a, b))

    target = len(remain)
    # 스도미노쿠 탐색 시작
    mark = False
    def dfs(level):
        global mark
        if mark == True:
            return
        if level == target:
            for p in puzzle:
                print("".join(map(str, p)))
            mark = True
            return
        x, y = remain[level]
        if puzzle[x][y]:
            dfs(level+1)


        # 도미노 고르기
        for a in range(1, 10):
            for b in range(1, 10):
                if a == b or check_dominos[a][b] == True:
                    continue
                if puzzle[x][y] == 0:
                    for k in range(2):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < 9 and 0 <= ny < 9 and puzzle[nx][ny] == 0:
                            if is_sdoku_1[x][a] == is_sdoku_2[y][a] == is_sdoku_3[(x//3)*3 + y//3][a] == is_sdoku_1[nx][b] == is_sdoku_2[ny][b] == is_sdoku_3[(nx//3)*3 + ny//3][b] == False:
                                check_dominos[a][b] = True
                                check_dominos[b][a] = True
                                is_sdoku_1[x][a], is_sdoku_2[y][a], is_sdoku_3[(x//3)*3 + y//3][a] = True, True, True
                                is_sdoku_1[nx][b], is_sdoku_2[ny][b], is_sdoku_3[(nx//3)*3 + ny//3][b] = True, True, True
                                puzzle[x][y] = a
                                puzzle[nx][ny] = b
                                dfs(level+1)
                                check_dominos[a][b] = False
                                check_dominos[b][a] = False
                                is_sdoku_1[x][a], is_sdoku_2[y][a], is_sdoku_3[(x//3)*3 + y//3][a] = False, False, False
                                is_sdoku_1[nx][b], is_sdoku_2[ny][b], is_sdoku_3[(nx//3)*3 + ny//3][b] = False, False, False
                                puzzle[x][y] = 0
                                puzzle[nx][ny] = 0

    dfs(0)

    P_NUM += 1