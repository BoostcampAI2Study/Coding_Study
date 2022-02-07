import itertools

N = int(input())
S = list(map(int, input().split()))
result = set(S)

for k in range(2, N + 1):
    for subseq in itertools.combinations(S, k):
        result.add(sum(subseq))

num = 1
result = sorted(list(result))
for i in result:
    if num == i:
        num += 1
        continue
    else:
        break
print(num)
