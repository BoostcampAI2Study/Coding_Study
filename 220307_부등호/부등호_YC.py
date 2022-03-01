from collections import deque

K = int(input())
signs = list(input().split())

queue = deque()

for num in range(10):
    queue.append((0,str(num)))

answer = []

while queue:
    idx, string = queue.popleft()

    if idx == K:
        answer.append(string)
        continue

    if signs[idx] =='>':
        for nums in range(int(string[-1])):
            if str(nums) not in string:
                queue.append((idx+1, string+str(nums)))

    else:
        for nums in range(9, int(string[-1]), -1):
            if str(nums) not in string:
                queue.append((idx+1, string+str(nums)))

print(max(answer))
print(min(answer))
