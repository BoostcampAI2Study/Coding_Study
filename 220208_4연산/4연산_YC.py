from collections import deque

def bfs(s,t):
    check=set()
    check.add(s)
    queue = deque([[s,'']])

    while queue:
        value, arr = queue.popleft()

        if value == t:
            return arr

        new_value = value*value
        if 1< new_value <= t and new_value not in check:
            check.add(new_value)
            queue.append([new_value,arr+'*'])
        
        new_value = value+value
        if 0<new_value <= t and new_value not in check:
            check.add(new_value)
            queue.append([new_value,arr+'+'])
        
        new_value = 1
        if new_value not in check:
            check.add(new_value)
            queue.append([new_value, arr+'/'])
        
def solution():
    s, t = map(int, input().split())
    
    if s == t:
        print(0)
        return

    a=bfs(s,t)

    if a:
        print(a)
    else:
        print(-1)

solution()