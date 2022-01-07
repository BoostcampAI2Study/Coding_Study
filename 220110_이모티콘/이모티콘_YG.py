from collections import deque
import sys
# 1. 이모티콘 모두 복사 & 클립보드에 저장
# 2. 클립보드 모든 이모티콘 붙여넣기
# 3. 이모티콘 하나 삭제
# 모든 연산 1초 걸림

input = sys.stdin.readline

S = int(input())

q = deque()

times = [[1e9]*1001 for _ in range(1001)]

q = deque()

# 스크린, 클립보드, 시간
q.append((1, 0, 0))
times[1][0] = 0

while q:
    screen, clip, time = q.popleft()

    # 1번
    if times[screen][screen] > time+1:
        times[screen][screen] = time+1
        q.append((screen, screen, time+1))

    # 2번
    if clip != 0 and screen+clip <= 1000:
        if times[screen+clip][clip] > time+1:
            times[screen+clip][clip] = time+1
            q.append((screen+clip, clip, time+1))

    # 3번
    if screen-1 >= 2:
        if times[screen-1][clip] > time+1:
            times[screen-1][clip] = time+1
            q.append((screen-1, clip, time+1))


print(min(times[S]))
