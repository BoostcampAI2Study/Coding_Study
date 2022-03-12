import sys
from collections import deque, defaultdict
import copy

input = sys.stdin.readline

hanoi = defaultdict(list)

abc_sum = 0
A, B, C = 0, 0, 0
A_str, B_str, C_str = "", "", ""
for idx in ['A', 'B', 'C']:
    stringg = input().rstrip()

    if stringg == '0':
        continue

    a, b = stringg.split()


    if idx == 'A':
        A += b.count(idx)
        A_str += b
    elif idx == 'B':
        B += b.count(idx)
        B_str += b
    else:
        C += b.count(idx)
        C_str += b

    abc_sum += int(a)

q = deque()

# 횟수
q.append((0, A_str, B_str, C_str, A, B, C))

visited = set()
visited.add(A_str+str(A)+B_str+str(B)+C_str+str(C))

# bfs 시작
while q:
    cnt, astr, bstr, cstr, aa, bb, cc = q.popleft()

    # top이 조건에 맞으면 출력하고 멈춤
    if aa + bb + cc == abc_sum:
        print(cnt)
        break

    # A -> B
    if astr:
        sub = astr[-1]
        astr = astr[:-1]
        bstr += sub

        if sub == 'A':
            code = astr+str(aa-1)+bstr+str(bb)+cstr+str(cc)
            if not code in visited:
                q.append((cnt+1, astr, bstr, cstr, aa-1, bb, cc))
                visited.add(code)
        elif sub == 'B':
            code = astr+str(aa)+bstr+str(bb+1)+cstr+str(cc)
            if not code in visited:
                q.append((cnt+1,  astr, bstr, cstr, aa, bb+1, cc))
                visited.add(code)
        else:
            code = astr+str(aa)+bstr+str(bb)+cstr+str(cc)
            if not code in visited:
                q.append((cnt+1,  astr, bstr, cstr, aa, bb, cc))
                visited.add(code)

        astr += sub
        bstr = bstr[:-1]

    # A -> C

    if astr:
        sub = astr[-1]
        astr = astr[:-1]
        cstr += sub

        if sub == 'A':
            code = astr+str(aa-1)+bstr+str(bb)+cstr+str(cc)
            if not code in visited:
                q.append((cnt+1, astr, bstr, cstr, aa-1, bb, cc))
                visited.add(code)
        elif sub == 'B':
            code = astr+str(aa)+bstr+str(bb)+cstr+str(cc)
            if not code in visited:
                q.append((cnt+1, astr, bstr, cstr, aa, bb, cc))
                visited.add(code)
        else:
            code = astr+str(aa)+bstr+str(bb)+cstr+str(cc+1)
            if not code in visited:
                q.append((cnt+1, astr, bstr, cstr, aa, bb, cc+1))
                visited.add(code)
        astr += sub
        cstr = cstr[:-1]


    # B -> A

    if bstr:
        sub = bstr[-1]
        bstr = bstr[:-1]
        astr += sub

        if sub == 'A':
            code = astr+str(aa+1)+bstr+str(bb)+cstr+str(cc)
            if not code in visited:
                q.append((cnt+1, astr, bstr, cstr, aa+1, bb, cc))
                visited.add(code)
        elif sub == 'B':
            code = astr+str(aa)+bstr+str(bb-1)+cstr+str(cc)
            if not code in visited:
                q.append((cnt+1, astr, bstr, cstr, aa, bb-1, cc))
                visited.add(code)
        else:
            code = astr+str(aa)+bstr+str(bb)+cstr+str(cc)
            if not code in visited:
                q.append((cnt+1, astr, bstr, cstr, aa, bb, cc))
                visited.add(code)

        bstr += sub
        astr = astr[:-1]

    # B -> C

    if bstr:
        sub = bstr[-1]
        bstr = bstr[:-1]
        cstr += sub

        if sub == 'A':
            code = astr+str(aa)+bstr+str(bb)+cstr+str(cc)
            if not code in visited:
                q.append((cnt+1, astr, bstr, cstr, aa, bb, cc))
                visited.add(code)
        elif sub == 'B':
            code = astr+str(aa)+bstr+str(bb-1)+cstr+str(cc)
            if not code in visited:
                q.append((cnt+1, astr, bstr, cstr, aa, bb-1, cc))
                visited.add(code)
        else:
            code = astr+str(aa)+bstr+str(bb)+cstr+str(cc+1)
            if not code in visited:
                q.append((cnt+1, astr, bstr, cstr, aa, bb, cc+1))
                visited.add(code)

        bstr += sub
        cstr = cstr[:-1]

    # C -> A

    if cstr:
        sub = cstr[-1]
        cstr = cstr[:-1]
        astr += sub

        if sub == 'A':
            code = astr+str(aa+1)+bstr+str(bb)+cstr+str(cc)
            if not code in visited:
                q.append((cnt+1, astr, bstr, cstr, aa+1, bb, cc))
                visited.add(code)
        elif sub == 'B':
            code = astr+str(aa)+bstr+str(bb)+cstr+str(cc)
            if not code in visited:
                q.append((cnt+1, astr, bstr, cstr, aa, bb, cc))
                visited.add(code)
        else:
            code = astr+str(aa)+bstr+str(bb)+cstr+str(cc-1)
            if not code in visited:
                q.append((cnt+1, astr, bstr, cstr, aa, bb, cc-1))
                visited.add(code)

        cstr += sub
        astr = astr[:-1]

    # C -> B

    if cstr:
        sub = cstr[-1]
        cstr = cstr[:-1]
        bstr += sub

        if sub == 'A':
            code = astr+str(aa)+bstr+str(bb)+cstr+str(cc)
            if not code in visited:
                q.append((cnt+1, astr, bstr, cstr, aa, bb, cc))
                visited.add(code)
        elif sub == 'B':
            code = astr+str(aa)+bstr+str(bb+1)+cstr+str(cc)
            if not code in visited:
                q.append((cnt+1, astr, bstr, cstr, aa, bb+1, cc))
                visited.add(code)
        else:
            code = astr+str(aa)+bstr+str(bb)+cstr+str(cc-1)
            if not code in visited:
                q.append((cnt+1, astr, bstr, cstr, aa, bb, cc-1))
                visited.add(code)
        cstr += sub
        bstr = bstr[:-1]