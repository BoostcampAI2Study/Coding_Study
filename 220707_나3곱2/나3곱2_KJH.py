# https://www.acmicpc.net/problem/16936

N = int(input())
num_list = list(map(int, input().split()))

# 각자 2와 3이 몇개 들어가는지 파악
# 2가 가장 적고, 3이 가장 많은 것

count_list = []
for num in num_list:
    exp = 1
    cnt2 = 0
    while not num % exp:
        exp *= 2
        cnt2 += 1
    exp = 1
    cnt3 = 0
    while not num % exp:
        exp *= 3
        cnt3 += 1
    count_list.append((cnt2 - 1, cnt3 - 1, num))

answer = []
for _, _, an in sorted(count_list, key=lambda x: (-x[1], x[0])):
    answer.append(str(an))
print(" ".join(answer))
