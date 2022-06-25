from itertools import combinations

n = int(input())
s = list(map(int, input().split()))

total = sum(s)

nums = set(s)
nums.add(total)

for count in range(1, n//2+1):
    for combi in combinations(s, count):
        num = sum(combi)
        nums.update((num, total-num))

answer = 1
while answer in nums:
    answer += 1

print(answer)




