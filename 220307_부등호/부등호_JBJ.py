import sys

K = int(sys.stdin.readline().strip())
COMPARISON_OPERATORS = sys.stdin.readline().strip().split()
max_num, min_num = '0'*K, '9'*K

def dfs(operators_idx, num):
    global max_num, min_num, COMPARISON_OPERATORS, K

    if operators_idx == K:
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        return

    for digit in range(10):
        if str(digit) not in num:
            if COMPARISON_OPERATORS[operators_idx] == '>' and num[-1] > str(digit):
                dfs(operators_idx+1, num+str(digit))
            elif COMPARISON_OPERATORS[operators_idx] == '<' and num[-1] < str(digit):
                dfs(operators_idx+1, num+str(digit))

for digit in range(10):
    dfs(0, str(digit))
    
print(max_num)
print(min_num)