def solution(S):
    queue = [(1, 2, 2)]
    result = 0
    visit = [[0 for i in range(1000)] for j in range(1000)]
    visit[0][1] = 1
    while queue:
        clip, tmp, time = queue.pop(0)
        if tmp == S:
            result = time
            break
        # copy
        if visit[tmp-1][tmp-1]==0:
            queue.append((tmp,tmp,time+1))
            visit[tmp - 1][tmp - 1] = 1
        # paste
        if (clip + tmp) <= 1000 and visit[clip-1][clip+tmp-1]==0:
            queue.append((clip,clip+tmp,time+1))
            visit[clip - 1][clip + tmp - 1] = 1
        # delete
        if tmp > 1 and visit[clip-1][tmp-2]==0:
            queue.append((clip,tmp-1,time+1))
            visit[clip - 1][tmp - 2] = 1

    return result