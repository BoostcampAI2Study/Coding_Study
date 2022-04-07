import sys, collections
S = int(sys.stdin.readline())
q = collections.deque()
q.append((1, 1))
visit = [[0] * S for _ in range(S)]
visit[0][0] = 1
while q:
    clip, screen = q.popleft()
    if screen == S:
        print(visit[clip - 1][screen - 1])
        break
    # copy
    if not visit[screen - 1][screen - 1]:
        q.append((screen, screen))
        visit[screen - 1][screen - 1] = visit[clip - 1][screen - 1] + 1
    # paste
    if (clip + screen) <= S and not visit[clip - 1][clip + screen - 1]:
        q.append((clip, clip + screen))
        visit[clip - 1][clip + screen - 1] = visit[clip - 1][screen - 1] + 1
    # delete
    if clip >= 1 and screen >= 2 and not visit[clip - 1][screen - 2]:
        q.append((clip, screen - 1))
        visit[clip - 1][screen - 2] = visit[clip - 1][screen - 1] + 1
