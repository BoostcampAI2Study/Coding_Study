import sys
ADDRESS = list(sys.stdin.readline().strip().replace('::', ':t:').split(':'))
for i in range(len(ADDRESS)):
    if ADDRESS[i] == '':
        del ADDRESS[i]
        break

zero_group_cnt = 9 - len(ADDRESS) if 't' in ADDRESS else 0
result = ''
cnt = 0
for i in range(8):
    if zero_group_cnt == 8:
        break
    if i < len(ADDRESS):
        if ADDRESS[i] != 't':
            result = result + ADDRESS[i].zfill(4) +':'
            cnt += 1
        else:
            for j in range(zero_group_cnt):
                result += '0000:'
            cnt += zero_group_cnt
print(result[:-1])
