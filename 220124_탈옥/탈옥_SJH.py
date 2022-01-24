from sys import stdin


def search(h, w, jail, exit, prisoner):
    move = ((1, 0), (-1, 0), (0, 1), (0, -1))
    total_door = set()

    def dfs(i, j, door=set()):
        min_door = set()

        if (i, j) in exit:
            return door

        for _i, _j in move:
            ni, nj = i+_i, j+_j
            
            # 범위 초과
            if not(-1 < ni < h and -1 < nj < w):
                continue
            
            # 이미 방문한 곳
            if visit[ni][nj]:
                continue
            
            # 벽
            if jail[ni][nj] == '*':
                continue
            
            # 방문 처리
            visit[ni][nj] = True

            # 빈공간
            if jail[ni][nj] == '.':
                open_door = dfs(ni, nj, door)                   
            
            # 문
            else:
                _door = door.copy()
                _door.add((ni, nj))
                open_door = dfs(ni, nj, _door)

            if not min_door or len(min_door) > len(open_door):
                min_door = open_door 

        return min_door



    for pi, pj in prisoner:
        visit = [[False] * w for _h in range(h)]
        visit[pi][pj] = True
        total_door |= dfs(pi, pj)

    return len(total_door)



if __name__ == '__main__':
    input = stdin.readline
    jail_count = int(input())
    answer = []

    # 감옥 수만큼 반복
    for j in range(jail_count):
        h, w = map(int, input().split())

        # 감옥 및 죄수, 출구 위치정보        
        jail = []
        prisoner = []
        exit = []
        for _h in range(h):
            # 감옥 정보
            jail.append(list(input()))
            _jail = jail[-1]
            
            # 출구 위치
            if 0 < _h < h-1:
                if _jail[0] == '#' or _jail[0] == '.':
                    exit.append((_h, 0))
                if _jail[-1] == '#' or _jail[-1] == '.':
                    exit.append((_h, w-1))
            else:
                for _w in range(w):
                    if _jail[_w] == '#' or _jail[_w] == '.':
                        exit.append((_h, _w))               

            # 죄수 위치 정보 다 가지고 있으면 넘어감
            if len(prisoner) > 1:
                continue
            
            # 죄수 위치
            for _w in range(w):
                if _jail[_w] == '$':
                    prisoner.append((_h, _w))
        
        # 최소 문 수 탐색
        answer.append(search(h, w, jail, exit, prisoner))

    print(*answer, sep='\n')