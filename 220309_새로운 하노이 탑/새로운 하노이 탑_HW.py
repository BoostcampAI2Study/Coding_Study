# ref: https://yabmoons.tistory.com/205
import collections

# input
input_bar_states = [input().split() for _ in range(3)]
bar_states = ""
for i in range(3):
    if int(input_bar_states[i][0]) == 0:
        input_bar_states[i].append("")

visit = set()
visit.add(input_bar_states[0][1] + "/" + input_bar_states[1][1] + "/" + input_bar_states[2][1])

# check visit
def check_visit(a, b, c):
    new_states = a + "/" + b + "/" + c
    if new_states in visit:
        return False
    visit.add(new_states)
    return True

# check answer
def check_answer(a, b, c):
    if 'B' in a or 'C' in a or 'A' in b or 'C' in b or 'A' in c or 'B' in c:
        return False
    else:
        return True
# bfs
q = collections.deque()
q.append((input_bar_states[0][1], input_bar_states[1][1], input_bar_states[2][1], 0))
while q:
    bar_a, bar_b, bar_c, move = q.popleft()
    # check answer
    check = True
    if check_answer(bar_a, bar_b, bar_c):
        print(move)
        break

    # append
    if len(bar_a) > 0:
        if check_visit(bar_a[:-1], bar_b + bar_a[-1], bar_c):
            q.append((bar_a[:-1], bar_b + bar_a[-1], bar_c, move + 1))
        if check_visit(bar_a[:-1], bar_b, bar_c + bar_a[-1]):
            q.append((bar_a[:-1], bar_b, bar_c + bar_a[-1], move + 1))
    if len(bar_b) > 0:
        if check_visit(bar_a + bar_b[-1], bar_b[:-1], bar_c):
            q.append((bar_a + bar_b[-1], bar_b[:-1], bar_c, move + 1))
        if check_visit(bar_a, bar_b[:-1], bar_c + bar_b[-1]):
            q.append((bar_a, bar_b[:-1], bar_c + bar_b[-1], move + 1))
    if len(bar_c) > 0:
        if check_visit(bar_a + bar_c[-1], bar_b, bar_c[:-1]):
            q.append((bar_a + bar_c[-1], bar_b, bar_c[:-1], move + 1))
        if check_visit(bar_a, bar_b + bar_c[-1], bar_c[:-1]):
            q.append((bar_a, bar_b + bar_c[-1], bar_c[:-1], move + 1))
