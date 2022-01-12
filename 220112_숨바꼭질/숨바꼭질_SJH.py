'''
걷거나 순간이동해서 동생 빨리찾기
위치 X일때 걸으면 X-1 또는 X+1, 순간이동하면 2*X
'''
from collections import deque

N, K = tuple(map(int, input().split()))

visit = [-1 for i in range(100001)]   # 방문체크 및 시간 기록
visit[N] = 0 # 시작점 표시 (수빈이 위치)
queue = deque([N])

# 범위 체크
def is_in_range(index):
    return -1 < index and index < 100001

# bfs 탐색
while queue:
    i = queue.popleft()
    next_indexs = [i-1, i+1, i*2]

    for ni in next_indexs:
        # 범위를 벗어났거나 첫 방문이 아닌 경우
        if not is_in_range(ni) or visit[ni] > -1:
            continue

        visit[ni] = visit[i] + 1

        # 동생 찾은 경우
        if ni == K:
            queue = None
            break

        queue.append(ni)

print(visit[K])