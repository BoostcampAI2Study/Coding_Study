def solution(N, K):
    queue = [(N, 0)]
    visit = [0 for i in range(100001)]
    visit[N] = 1
    result = 0
    while queue:
        tmp, time = queue.pop(0)
        if tmp == K:
            result = time
            break
        if tmp <= 50000 and visit[2*tmp]!=1:
            queue.append((2*tmp, time + 1))
            visit[2*tmp]=1
        if tmp > 0 and visit[tmp-1]!=1:
            queue.append((tmp-1,time+1))
            visit[tmp - 1] = 1
        if tmp < 100000 and visit[tmp+1]!=1:
            queue.append((tmp + 1, time + 1))
            visit[tmp + 1] = 1

    return result