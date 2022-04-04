import itertools, sys

N = int(sys.stdin.readline().rstrip())
S = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

already_teamed_up = set()
min_diff = sys.maxsize
for teammates in itertools.combinations(range(N), N//2):
    opponents = set(range(N)) - set(teammates)

    if teammates in already_teamed_up: continue # bactracking (6016ms -> 3180ms)
    else: already_teamed_up.add(tuple(opponents))

    opponents_sum, teammates_sum = 0, 0
    for i, j in itertools.combinations(teammates, 2):
        teammates_sum += (S[i][j] + S[j][i])
    for i, j in itertools.combinations(opponents, 2):
        opponents_sum += (S[i][j] + S[j][i])

    min_diff = min(abs(teammates_sum-opponents_sum), min_diff)
print(min_diff)