import itertools, sys
N = int(sys.stdin.readline())
sum_dict = set()
for sequence in itertools.combinations_with_replacement([1, 5, 10, 50], N):
    sum_dict.add(sum(sequence))
print(len(sum_dict))
