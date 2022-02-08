import sys
cube = list(map(int, input().split()))
opposite_dict = {0: 8, 4: 20, 12: 16}

# 마주보는 면이 각각 일정 색으로 채워져 있는지 확인. (단, 해당 경우는 하나만 존재)
cnt = 0
remove_side = -1
for i in [0, 4, 12]:
    opposite = opposite_dict[i]
    if len(set(cube[i:i + 4])) == 1 and len(set(cube[opposite:opposite + 4])) == 1:
        remove_side = i
        cnt += 1
if cnt != 1:
    print(0)
    sys.exit()

# 고정된 면을 제외하고 큐브 이동시 조건 충족 하는지 확인
first_colors = []
second_colors = []
check_cube = False
if remove_side == 0:
    # 가로가 동일한지 확인
    for i in [12, 4, 16, 20]:
        if cube[i] != cube[i + 1] or cube[i + 2] != cube[i + 3]:
            check_cube = True
        else:
            first_colors.append(cube[i])
            second_colors.append(cube[i + 2])
elif remove_side == 4:
    # 가로, 세로 동일 확인
    for i in [0, 8]:
        if cube[i] != cube[i + 1] or cube[i + 2] != cube[i + 3]:
            check_cube = True
    for i in [12, 16]:
        if cube[i] != cube[i + 2] or cube[i + 1] != cube[i + 3]:
            check_cube = True
    first_colors = [cube[0], cube[17], cube[10], cube[12]]
    second_colors = [cube[2], cube[16], cube[8], cube[13]]
else:
    # 세로 확인
    for i in [0, 4, 8, 20]:
        if cube[i] != cube[i + 2]:
            check_cube = True
    first_colors = [cube[0], cube[4], cube[8], cube[21]]
    second_colors = [cube[1], cube[5], cube[9], cube[20]]
if len(set(first_colors)) != 4 or check_cube:
    print(0)
    sys.exit()

# 큐브 이동
for i in range(3):
    if first_colors[i] == second_colors[i + 1]:
        check_cube = True
    else:
        break
if check_cube:
    print(1)
    sys.exit()

for i in range(3):
    if first_colors[i + 1] == second_colors[i]:
        check_cube = True
    else:
        break

print(1) if check_cube else print(0)