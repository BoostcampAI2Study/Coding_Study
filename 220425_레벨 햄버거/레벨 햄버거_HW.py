import sys
N, X = map(int, sys.stdin.readline().split())

level_burgers = [(1, 1, 0)]  # length, patty, burn
for i in range(1, N + 1):
    final_burger_len = 3 + level_burgers[i - 1][0] * 2
    patty, burn = level_burgers[i - 1][1] * 2 + 1, level_burgers[i - 1][1] * 2 + 2
    level_burgers.append((final_burger_len, patty, burn))

def get_eat_patty(eat_range, level):
    if level == 0:
        return 1
    if eat_range == 1:
        return 0
    elif eat_range <= level_burgers[level - 1][0] + 1:
        return get_eat_patty(eat_range - 1, level - 1)
    elif eat_range == level_burgers[level][0] // 2 + 1:
        return level_burgers[level - 1][1] + 1
    elif eat_range <= level_burgers[level][0] - 1:
        return get_eat_patty(eat_range - level_burgers[level - 1][0] - 2, level - 1) + level_burgers[level - 1][1] + 1
    elif eat_range == level_burgers[level][0]:
        return level_burgers[level][1]

print(get_eat_patty(X, N))
