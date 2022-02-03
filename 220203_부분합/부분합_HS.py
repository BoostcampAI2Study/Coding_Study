N, S = list(map(int, input().split()))
arr = list(map(int, input().split()))

answer = 100001 # 100,001
start, end = 0, 0
# partial sum
partial_sum = arr[0]

while end < len(arr):
    # if partial sum > S,
    if partial_sum >= S:
        # update answer and reduce the section by [start + 1]
        answer = min(answer, end - start + 1)
        partial_sum -= arr[start]
        start += 1
    # Limit the length of the current section
    elif end - start + 1 >= answer:
        partial_sum -= arr[start]
        start += 1
    # Exploring by [end + 1]
    else:
        end += 1
        try:
            partial_sum += arr[end]
        except:
            pass
# Exception
if answer == 100001:
    print(0)
else:
    print(answer)

# Language        : Python3
# Memory          : 42028 kb
# Time            : 168 ms
# Time complexity : almost O(N)