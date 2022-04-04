import sys, collections
T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

result = 0
sum_A = collections.defaultdict(int)
for i in range(len(A)):
    for j in range(i, len(A)):
        sum_A[sum(A[i:j + 1])] += 1

for i in range(len(B)):
    for j in range(i, len(B)):
        result += sum_A[T - sum(B[i:j + 1])]
print(result)
