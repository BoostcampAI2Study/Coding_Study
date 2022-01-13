import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

answer = 0

right = 0
left = 1

result = arr[0]

while right < left < len(arr):  
    if result > M:
        result-=arr[right]
        right +=1
    else:
        if result == M:
            answer+=1
        result+=arr[left]
        left +=1

print(answer)