from collections import deque

def solution(A,B,C):
    if A==B and B==C:
        print(1)
        return 
    if (A+B+C) % 3:
        print(0)
        return 
    if ((A+B+C)/3) % 2:
        print(0)
        return

    total = A+B+C
    visited = [[False for _ in range(total)] for _ in range(total)]

    queue = deque([[A,B]])

    while queue:
        a, b = queue.popleft()
        c = total-(a+b)

        for x, y in ([a,b],[b,c],[c,a]):
            if x > y:
                x-=y
                y+=y
            elif x < y:
                x+=x
                y-=x
            else:
                continue

            z = total-(x+y)

            if x==y and y==z:
                print(1)
                return
                
            if x>0 and y>0 and z>0 and not visited[min(x, y, z)][max(x, y, z)]:
                visited[min(x, y, z)][max(x, y, z)] = True
                queue.append([x,y])
    print(0)
    return

A, B, C = map(int, input().split())

solution(A, B, C)