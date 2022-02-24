import itertools
test_cases = []
idx = 0
# input
while True:
    test_cases.append(list(map(int, input().split())))
    if test_cases[idx][0] == 0:
        break
    idx += 1
# 경우의 수 
for i in range(idx):
    test_case = test_cases[i][1:]
    for case in list(itertools.combinations(test_case, 6)):
        case = map(str, case)
        print(' '.join(case))
    print()
