import sys, collections

S = int(sys.stdin.readline())
Q = collections.deque()

times = [[sys.maxsize]*(S+1) for _ in range(S+1)]
times[1][0] = 0

# (screen, clipboard)
Q.append((1, 0))

while Q:  
    screen, clipboard = Q.popleft()
    cur_time = times[screen][clipboard]

    # Operation 1 - save all screen emojis to clipboard.
    if times[screen][screen] == sys.maxsize:
        times[screen][screen] = cur_time + 1
        Q.append((screen, screen))
    
    # Operation 2 - paste screen emojis from clipboard.
    if S >= (screen + clipboard) and times[screen+clipboard][clipboard] == sys.maxsize:
        times[screen+clipboard][clipboard] = cur_time + 1
        Q.append((screen+clipboard, clipboard))
    
    # Operation 3 - delete one of the screen emojis from screen.
    if (screen - 1) >= 2 and times[screen-1][clipboard] == sys.maxsize:
        times[screen-1][clipboard] = cur_time + 1
        Q.append((screen-1, clipboard))       

print(min(times[S]))