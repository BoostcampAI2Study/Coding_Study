import sys

def Migration(N,M,A) :
    pass

# 문제정의
# 인구 이동이 지속 되는 날짜 Count
# contries[i][j]와 인접한 contries[i+1][j], contries[i][j+1]를 비교했을 때 L 이상, R 이하일 때만 연합
# 연합을 이룬 나라의 인구수는 (연합 전체 인구 수) / (연합 나라 수) 로 재조정
# 문제 접근
# 1. 연합된 나라의 위치, 개수를 어떻게 파악할 것인가
# 2. 인구 수 비교를 어떤 기준으로 해야 가장 빠르게 할 수 있을까
# 어제 오늘 이사하느라 많이 고민하지 못했습니당 ㅜㅜ 주말에 다시 풀어볼게용!


N, L, R = map(int, sys.stdin.readline().split())
contries = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

print(Migration(N, L, R, contries))

