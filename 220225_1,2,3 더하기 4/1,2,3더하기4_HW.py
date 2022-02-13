T = int(input())
test_num = [int(input()) for _ in range(T)]

def count_sum(num):
    cnt = 1     # [1]
    for k in range(2):
        # [2], [3]
        if num % (k + 2) == 0:
            cnt += 1
        # [1, 2], [1, 3]
        if num // (k + 2):
            if num % (k + 2) == 0:
                cnt += (num // (k + 2)) - 1
            else:
                cnt += (num // (k + 2))

    div = num // 3
    for k in range(div):
        num -= 3
        if num <= 0:
            break
        # [2, 3]
        if num % 2 == 0:
            cnt += 1
        # [1, 2, 3]
        if num // 2:
            if num % 2 == 0:
                cnt += (num // 2) - 1
            else:
                cnt += (num // 2)
    return cnt

for i in range(T):
    print(count_sum(test_num[i]))
