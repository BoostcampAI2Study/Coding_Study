import sys

def get_value(v1, v2, symbol):
    if symbol == '*':
        return v1 * v2
    elif symbol == '+':
        return v1 + v2
    else:
        return v1 - v2

def postfix_cal(exp):
    operators, nums = [], []
    for i in range(len(exp)):
        if '0' <= exp[i] <= '9':
            nums.append(int(exp[i]))
        else:
            if exp[i] == '(':
                operators.append(exp[i])
            elif exp[i] == ')':
                while operators[-1] != '(':
                    n1 = nums.pop()
                    nums.append(get_value(nums.pop(), n1, operators.pop()))
                operators.pop()
            else:
                while True:
                    if len(operators) == 0:
                        operators.append(exp[i])
                        break
                    if operators[-1] == '(' or (operators[-1] != '*' and exp[i] == '*'):
                        operators.append(exp[i])
                        break
                    else:
                        n1 = nums.pop()
                        nums.append(get_value(nums.pop(), n1, operators.pop()))
    while operators:
        n1 = nums.pop()
        nums.append(get_value(nums.pop(), n1, operators.pop()))

    return nums[0]

def calculate(i, exp):
    global result
    if i >= (N // 2):
        if exp[-1] != ')':
            exp += EXPRESSION[N - 1]
        result = max(result, postfix_cal(exp))
        return
    if exp != "" and exp[-1] == ')':
        calculate(i + 1, exp + EXPRESSION[2 * i + 1])
    else:
        calculate(i + 1, exp + EXPRESSION[2 * i] + EXPRESSION[2 * i + 1])
        calculate(i + 1, exp + '(' + EXPRESSION[2 * i] + EXPRESSION[2 * i + 1] + EXPRESSION[2 * i + 2] + ')')

N = int(sys.stdin.readline())
EXPRESSION = sys.stdin.readline().strip()
result = -2**31
        
if N == 1:
    print(EXPRESSION[0])
else:
    calculate(0, "")
    print(result)
