plate_cnt, prev_char = 1, ''
for cur_char in input().rstrip():
    case = 26 if cur_char == 'c' else 10
    plate_cnt *= (case - 1) if cur_char == prev_char else case
    prev_char = cur_char

print(plate_cnt)
