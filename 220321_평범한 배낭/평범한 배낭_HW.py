N, K = map(int, input().split())
stuff_info = [list(map(int, input().split())) for _ in range(N)]

bag = [[0] * (K + 1) for _ in range(N + 1)]
for stuff in range(1, N + 1):
    for weight in range(1, K + 1):
        if stuff_info[stuff - 1][0] <= weight:
            bag[stuff][weight] = max(stuff_info[stuff - 1][1] + bag[stuff - 1][weight - stuff_info[stuff - 1][0]],
                                     bag[stuff - 1][weight])
        else:
            bag[stuff][weight] = bag[stuff - 1][weight]
            
print(max(max(bag)))
