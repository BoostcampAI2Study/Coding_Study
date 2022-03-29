from collections import defaultdict

def operate(arr):
    new_arr = []
    max_length= 0

    for row in arr:
        new_row=[]
        counts = defaultdict(list)
        numbers = set(row)

        for num in numbers:
            if num != 0:
                counts[row.count(num)].append(num)

        for c in sorted(counts):
            for number in sorted(counts[c]):
                new_row.extend([number,c])

        new_arr.append(new_row[:100])
        max_length = max(max_length, len(new_row))

    max_length = min(100, max_length)

    for row in new_arr:
        if len(row) < max_length:
            row+=[0] * (max_length - len(row))
    
    return new_arr

def solution():
    r, c, k = map(int, input().split())

    ARRAY = [list(map(int, input().split())) for _ in range(3)]

    for t in range(101):
        if r-1 < len(ARRAY) and c-1 < len(ARRAY[0]) and ARRAY[r-1][c-1] == k:
            return t

        if len(ARRAY)>=len(ARRAY[0]):
            new_arr = operate(ARRAY)
        else:
            ARRAY = list(map(list, zip(*reversed(ARRAY))))
            new_arr = list(map(list, zip(*operate(ARRAY))))
        
        ARRAY = new_arr
    return -1

print(solution())
