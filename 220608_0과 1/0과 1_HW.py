import sys, collections
T = int(sys.stdin.readline())
N_LIST = [int(sys.stdin.readline()) for _ in range(T)]
visit = [0] * T

def bfs(num):
    visit = [False] * 20001
    q = collections.deque()
    q.append('1')
    while q:
        cur_num = q.popleft()
        candidates = [0] * 2
        for i in range(2):
            candidates[i] = (int(cur_num) * 10 + i) % num
            if not visit[candidates[i]]:
                if candidates[i] == 0:
                    return cur_num + str(i)

                visit[candidates[i]] = True
                q.append(cur_num + str(i))
    return 'BRAK'

for num in N_LIST:
    print(bfs(num))
