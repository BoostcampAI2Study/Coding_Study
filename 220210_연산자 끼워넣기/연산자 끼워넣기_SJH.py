from sys import stdin
from itertools import permutations

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return int(a / b)


input = stdin.readline
n = int(input())
nums = list(map(int, input().split()))
op_num = list(map(int, input().split()))
op_order = [add, sub, mul, div]
op_list = []

for i, o in enumerate(op_num):
    op_list.extend([op_order[i]] * o)

min_num = float('inf')
max_num = float('-inf')

for op_pm in set(permutations(op_list, n-1)):
    result = nums[0]
    for i, op in enumerate(op_pm):
        result = op(result, nums[i+1])
    min_num = min(result, min_num)
    max_num = max(result, max_num)

print(max_num)
print(min_num)