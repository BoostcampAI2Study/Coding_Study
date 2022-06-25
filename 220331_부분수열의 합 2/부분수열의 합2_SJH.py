from sys import stdin
from itertools import combinations
from collections import defaultdict

input = stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))


# 부분수열 합 구하기
def get_sub_sum(arr:list, result:defaultdict):
    for count in range(1, len(arr)+1):
        for combi in combinations(arr, count):
            c_sum = sum(combi)
            result[c_sum] += 1


# defaultdict를 이용해서 특정 합이 나오는 경우의 수 count
sub_sum1 = defaultdict(int)
sub_sum2 = defaultdict(int)

get_sub_sum(arr[n//2:], sub_sum1)
get_sub_sum(arr[:n//2], sub_sum2)

# 각 부분 수열에 S가 있는 경우 구하기
answer = sub_sum1[s] + sub_sum2[s]


# 두 부분수열을 더해서 S가 나오는 경우의 수 구하기
for s1 in sub_sum1:
    if s-s1 in sub_sum2:
        answer += sub_sum1[s1] * sub_sum2[s-s1]


print(answer)