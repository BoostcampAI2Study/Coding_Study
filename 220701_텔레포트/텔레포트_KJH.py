import sys

input = sys.stdin.readline

N, T = map(int, input().split())

cities = [list(map(int, input().split())) for _ in range(N)]
telpo_cities = [(idx, x, y) for idx, (s, x, y) in enumerate(cities) if s]

M = int(input())


def near_telpo(x, y):
    dist, near_node = float("inf"), None
    for node, tx, ty in telpo_cities:
        if dist > abs(x - tx) + abs(y - ty):
            near_node = node
            dist = abs(x - tx) + abs(y - ty)
    return near_node


for _ in range(M):
    A, B = map(int, input().split())
    A, B = A - 1, B - 1
    near_tel1, near_tel2 = near_telpo(cities[A][1], cities[A][2]), near_telpo(
        cities[B][1], cities[B][2]
    )
    print(
        min(
            abs(cities[A][1] - cities[B][1]) + abs(cities[A][2] - cities[B][2]),
            T
            + abs(cities[A][1] - cities[near_tel1][1])
            + abs(cities[A][2] - cities[near_tel1][2])
            + abs(cities[near_tel2][1] - cities[B][1])
            + abs(cities[near_tel2][2] - cities[B][2]),
        )
    )
