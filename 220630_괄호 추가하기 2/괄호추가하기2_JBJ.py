import sys
sys.setrecursionlimit(10**6)

N = int(input())
EXP = input()
max_value = sys.maxsize * -1

def dfs(operator_idx, new_exp):
    global N, EXP, max_value

    if operator_idx > N//2:
        max_value = max(max_value, eval(new_exp))
        return

    if new_exp[-1] != ')':
        dfs(operator_idx+1, new_exp[:-1] + '(' + new_exp[-1] + EXP[operator_idx*2-1:operator_idx*2+1] + ')')
    dfs(operator_idx+1, new_exp + EXP[operator_idx*2-1:operator_idx*2+1])

dfs(1, EXP[0])
print(max_value)