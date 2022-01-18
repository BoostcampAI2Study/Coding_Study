# 문제정의
# 인구 이동이 지속 되는 날짜 Count
# contries[i][j]와 인접한 contries[i+1][j], c를ontries[i][j+1] 비교했을 때 L 이상, R 이하일 때만 연합
# 연합을 이룬 나라의 인구수는 (연합 전체 인구 수) / (연합 나라 수) 로 재조정
# 문제 접근
# 1. 연합된 나라의 위치, 개수를 어떻게 파악할 것인가
# 2. 인구 수 비교를 어떤 기준으로 해야 가장 빠르게 할 수 있을까
# 어제 오늘 이사하느라 많이 고민하지 못했습니당 ㅜㅜ 주말에 다시 풀어볼게용!

import sys

def Migration(N, L, R, contries) :
    days = 0
    flag = False
    while True:
        check = 0
        check_union = [[-1 for _ in range(N)] for _ in range(N)]
        population = [0 for _ in range(N)]
        union = [0 for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if i < N-1:
                    if L <= abs(contries[i][j] - contries[i+1][j]) <= R:
                        if check_union[i][j] == -1 and check_union[i+1][j] == -1:
                            check_union[i][j] = check
                            check_union[i+1][j] = check
                            union[check] = 2
                            population[check] += contries[i][j] + contries[i+1][j]
                        else :
                            flag = True
                            if check_union[i][j] == -1:
                                check_union[i][j] = check_union[i+1][j]
                                union[check_union[i][j]] += 1
                                population[check_union[i+1][j]] += contries[i][j]
                                
                            else : 
                                check_union[i+1][j] = check_union[i][j]
                                union[check_union[i+1][j]] += 1
                                population[check_union[i][j]] += contries[i+1][j]
                if j < N-1:
                    if L <= abs(contries[i][j] - contries[i][j+1]) <= R:
                        if check_union[i][j] == -1 and check_union[i][j+1] == -1:
                            check_union[i][j] = check
                            check_union[i][j+1] = check
                            union[check] = 2
                            population[check] += contries[i][j] + contries[i][j+1]
                        else :
                            flag = True
                            if check_union[i][j] == -1:
                                check_union[i][j] = check_union[i][j+1]
                                union[check_union[i][j]] += 1
                                population[check_union[i][j+1]] += contries[i][j]
                            else : 
                                check_union[i][j+1] = check_union[i][j]
                                union[check_union[i][j+1]] += 1
                                population[check_union[i][j]] += contries[i][j+1]
                if flag:
                    check +=1
                    flag = False

        if union == [0 for _ in range(N)]:
            return days
        for n in range(N):
            if union[n] :
                population[n] = population[n] / union[n]
            
        for i in range(N):
            for j in range(N):
                if check_union[i][j] != -1:
                    contries[i][j] = population[check_union[i][j]]     
        days+=1     



N, L, R = map(int, sys.stdin.readline().split())
contries = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

print(Migration(N, L, R, contries))

