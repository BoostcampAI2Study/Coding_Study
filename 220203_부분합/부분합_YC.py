import sys
input = sys.stdin.readline

N,S = map(int, input().split())

lst = list(map(int, input().split()))

start = 0
end = 0

s = 0

length = 100000001

while True:
    if s >= S:
        if end-start < length:
            length = end - start
        s-=lst[start]
        start+=1
    elif end == N:
        break
    else:
        s+=lst[end]
        end+=1

if length == 100000001: print(0)
else: print(length)