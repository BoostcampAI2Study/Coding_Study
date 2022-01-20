from sys import stdin
from typing import List
import heapq as hq


def tree_life(N:int, year:int, s2d2_map:List, tree_info:List):
    ground = [[[] for n in range(N)] for n in range(N)] # 땅
    fertilizer = [[5 for n in range(N)] for n in range(N)]    # 비료 정보
    near = (
                (-1, -1), (-1, 0), (-1, 1), (0, -1),
                (0, 1), (1, -1), (1, 0), (1, 1)
            )   # 인접한 땅 정보 (번식할 때 사용)

    # 각 나무를 땅에 심는다
    for r, c, old in tree_info:
        ground[r-1][c-1].append(old)

    # 각 나무를 나이순으로 정렬한다
    for r in range(N):
        for c in range(N):
            hq.heapify(ground[r][c])            

    
    def spring_summer():
        for r in range(N):
            for c in range(N):
                fertilizer_index = -1   # 여름에 비료 될 나무 시작 인덱스                
                get_older = []  # 나이를 먹을 나무들

                for t in range(len(ground[r][c])):
                    # 이 자리에 있던 나무 목록 저장
                    _tree = ground[r][c][:]

                    # 나이가 어린 나무부터 먹는다
                    old = hq.heappop(ground[r][c])
                    
                    # 양분을 먹을 수 없는 나무는 즉시 죽는다
                    if old > fertilizer[r][c]:
                        fertilizer_index = t
                        break
                    else:
                        # 나무가 자신의 나이만큼 양분을 먹는다
                        fertilizer[r][c] -= old
                        
                        # 양분 먹으면 나이가 1 증가한다
                        old += 1
                        get_older.append(old)
                        
                        # 가을에 번식할 나무 (나이가 5의 배수)
                        if old % 5 == 0:
                            breeding_info.append((r, c))

                # 죽은 나무 있으면 비료 추가 (여름)
                if fertilizer_index > -1:
                    for old in _tree[fertilizer_index:]:
                        fertilizer[r][c] += old // 2

                # 살아남은 나무들만 남기기
                hq.heapify(get_older)
                ground[r][c] = get_older


    def fall():
        # 인접한 8개의 칸에 나이가 1인 나무가 생긴다
        for r, c in breeding_info:
            for _r, _c in near:
                nr, nc = r+_r, c+_c
                if -1 < nr < N  and -1 < nc < N:
                    hq.heappush(ground[nr][nc], 1)


    def winter():
        # S2D2가 땅을 돌아다니면서 양분을 추가한다
        for r in range(N):
            for c in range(N):
                fertilizer[r][c] += s2d2_map[r][c]
    

    # K년동안 4계절 보내기
    for y in range(year):
        breeding_info = []  # 가을에 번식할 나무 정보 (위치)
        spring_summer()
        fall()
        winter()

    # 살아있는 나무 수 세기
    tree_count = 0

    for r in range(N):
        for c in range(N):
            tree_count += len(ground[r][c])

    return tree_count



if __name__ == '__main__':
    input = stdin.readline
    N, M, K = map(int, input().split())
    A = [list(map(int, input().split())) for n in range(N)]
    tree_info = [list(map(int, input().split())) for m in range(M)]
    print(tree_life(N, K, A, tree_info))