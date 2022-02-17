from collections import deque


A, B, C = map(int, input().split())
check = set()
q = deque([[A, B, C]])
answer = 0
count = 0

def cal(x, y):
    return 2*x, y-x


while q and count < 1e5:
    a, b, c = q.popleft()

    if a == b == c:
        answer = 1
        break
    
    if a != b:
        _a, _b = cal(*sorted([a, b]))

        result = (_a, _b, c)
        if result not in check:
            check.add(result)
            q.append(result)

    if a != c:
        _a, _c = cal(*sorted([a, c]))
        
        result = (_a, b, _c)
        if result not in check:
            check.add(result)
            q.append(result)

    if b != c:
        _b, _c = cal(*sorted([b, c]))

        result = (a, _b, _c)
        if result not in check:
            check.add(result)
            q.append(result)
    
    count += 1


print(answer)