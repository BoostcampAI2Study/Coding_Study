from collections import deque
def solution(answer):
    q = deque()
    cur_sum = 0
    for val in arr:
        val = int(val)
        cur_sum += val
        q.append(val)
        while cur_sum > M:
            cur_sum -= q.popleft()
        if cur_sum == M:
            answer += 1
    return answer

if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = input().split()
    print(solution(0))