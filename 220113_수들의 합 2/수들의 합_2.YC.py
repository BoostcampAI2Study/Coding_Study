import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

left = 0
right = 1

answer = 0

result = arr[0]

while True:
    if result < M and right == N: break

    if result < M and right < N:
        result+=arr[right]
        right+=1
    else:
        while left <= right and result >= M:
            if result == M:
                answer+=1
            result-=arr[left]
            left+=1
print(answer)