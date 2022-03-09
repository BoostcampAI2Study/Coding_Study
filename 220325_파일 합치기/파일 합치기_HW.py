# https://developerbee.tistory.com/97
# 부분합 어떻게 더해야하나 고민, 블로그 참고함
import sys
def solution(k, case):
    chapter_sum = [[0] * k for _ in range(k)]

    for i in range(1, k):
        for start in range(k - i):
            end = start + i
            psum = sum(case[start:end + 1])
            chapter_sum[start][end] = sys.maxsize
            for n in range(start, end):
                chapter_sum[start][end] = min(chapter_sum[start][end], chapter_sum[start][n] + chapter_sum[n + 1][end] + psum)
    print(chapter_sum[0][k - 1])

T = int(input())
test_cases = []
for i in range(T):
    test_cases.append((int(input()), list(map(int, input().split()))))

for i in range(T):
    K, test_case = test_cases[i]
    solution(K, test_case)
