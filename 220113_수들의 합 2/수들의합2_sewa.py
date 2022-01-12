import sys

def Cases(N,M,A) :
    cases = 0
    start, end = 0, 1

    while end <= N and start <= end :
        total = sum(A[start:end])
        if total < M :  # 목표 합 보다 작으면, 하나 더 포함
            end += 1
        elif total > M :  # 목표 합 보다 크면, 하나 더 제외
            start += 1
        else : # total == M / 목표 합 도달, case 추가 후 새로운 기준으로 시작
            cases += 1
            start += 1        
    return cases


N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

print(Cases(N,M,A))


# 두 개 포인터 필요
# 이중 for문은 너무 오래걸리므로 이동에 기준을 둬 이동 범위를 줄이자
