import sys
sys.setrecursionlimit(10**6)
from collections import deque

input = sys.stdin.readline

answer =0
N, L, R = map(int, input().split())

A = []
for _ in range (N):
    A.append(list(map(int, input().split())))

def func1(i,j,united):
    visited[i][j] = True
    united.append([i,j])

    if j < N-1 and L<=abs(A[i][j] - A[i][j+1]) <=R:
        if not visited[i][j+1]:
            func1(i,j+1,united)

    if i < N-1 and L<=abs(A[i][j] - A[i+1][j]) <=R:
        if not visited[i+1][j]:
            func1(i+1,j,united)

    if j > 0 and L<=abs(A[i][j] - A[i][j-1]) <=R:
        if not visited[i][j-1]:
            func1(i,j-1,united)

    if i > 0 and L<=abs(A[i][j] - A[i-1][j]) <=R:
        if not visited[i-1][j]:
            func1(i-1,j,united)

while True:
    visited = [[False]*51 for i in range(51)]
    countries=[]

    for i in range(N):
        for j in range(N):
            united=[]
            if not visited[i][j]:
                func1(i,j,united)
            if united:
                countries.append(united)
    

    if len(countries) == N*N:
        break

    answer+=1

    for united in countries:
        if len(united) > 1:
            # calculate new population
            new_p=0
            for (i,j) in united:
                new_p += A[i][j]
            new_p=new_p//len(united)

            # update new population
            for (i,j) in united:
                A[i][j] = new_p

print(answer)