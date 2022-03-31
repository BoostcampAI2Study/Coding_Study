# prime_num에 1~9999 소수여부 저장 → bfs로 최소 이동횟수 계산
import sys, collections
T = int(sys.stdin.readline())
test_cases = [list(sys.stdin.readline().split()) for _ in range(T)]

# prime number check
prime_num = [True] * 10000
prime_num[1] = False
for num in range(2, int(10000 ** 0.5) + 1):
    if prime_num[num]:
        for i in range(2 * num, 10000, num):
            prime_num[i] = False

for t in range(T):
    min_move = -1
    start_pwd, end_pwd = test_cases[t][0], int(test_cases[t][1])

    q = collections.deque()
    q.append((start_pwd, 0))
    visit = [False] * 10000
    visit[int(start_pwd)] = True

    while q:
        cur_pwd, move = q.popleft()
        if int(cur_pwd) == end_pwd:
            min_move = move
            break
        for idx in range(4):
            for num in range(10):
                new_pwd = cur_pwd[:idx] + str(num) + cur_pwd[(idx + 1):]
                new_pwd_int = int(new_pwd)
                if 999 < new_pwd_int and not visit[new_pwd_int] and prime_num[new_pwd_int]:
                    q.append((new_pwd, move + 1))
                    visit[new_pwd_int] = True

    print(min_move)
