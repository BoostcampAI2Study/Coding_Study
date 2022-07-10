N = int(sys.stdin.readline())
S, W = [], []
for _ in range(N):
    s, w = map(int, sys.stdin.readline().split())
    S.append(s)
    W.append(w)

result = 0
def dfs(idx):
    global result
    if idx == N:
        cnt = 0
        for s in S:
            if s <= 0:
                cnt += 1
        result = max(result, cnt)
        return

    if S[idx] <= 0:
        dfs(idx + 1)
        return

    is_all_broken = True
    hand_s, hand_w = S[idx], W[idx]
    for j in range(N):
        other_s = S[j]
        if j != idx and other_s > 0:
            is_all_broken = False
            S[idx], S[j] = hand_s - W[j], other_s - W[idx]
            dfs(idx + 1)
            S[idx], S[j] = hand_s, other_s
    if is_all_broken:
        dfs(idx + 1)
dfs(0)
print(result)
