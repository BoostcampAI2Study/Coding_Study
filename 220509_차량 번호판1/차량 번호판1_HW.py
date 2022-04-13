import sys
SYMBOL_FORMAT = sys.stdin.readline().strip()

cases_cnt = 1
for idx in range(len(SYMBOL_FORMAT)):
    case = 26 if SYMBOL_FORMAT[idx] == 'c' else 10
    cases_cnt *= (case - 1) if idx > 0 and SYMBOL_FORMAT[idx - 1] == SYMBOL_FORMAT[idx] else case
print(cases_cnt)
