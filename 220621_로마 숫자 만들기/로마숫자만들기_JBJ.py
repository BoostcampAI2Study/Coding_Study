import itertools

N = int(input())
print(len({sum(cwr) for cwr in itertools.combinations_with_replacement((1, 5, 10, 50), N)}))
