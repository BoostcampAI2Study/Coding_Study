import sys

N, S = map(int, sys.stdin.readline().strip().split())
NUM_LIST = list(map(int, sys.stdin.readline().strip().split()))
left_ptr, right_ptr, num_list_len = 0, 0, len(NUM_LIST)
min_length, sum_ = sys.maxsize, NUM_LIST[0]

# expand (right ptr) first and then contract (left ptr) afterwards.
while True:
    if sum_ < S:
        right_ptr += 1
        if right_ptr >= num_list_len: break
        sum_ += NUM_LIST[right_ptr]
    else:
        sum_ -= NUM_LIST[left_ptr]
        min_length = min(min_length, right_ptr-left_ptr+1)
        left_ptr += 1
        
print(min_length if min_length != sys.maxsize else 0)
            