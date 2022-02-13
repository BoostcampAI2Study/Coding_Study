
N = int(input())
num_list = list(map(int, input().split()))
operator = list(map(int, input().split()))

answer_max = -1000000000 # -billion
answer_min = 1000000000 # billion
# Exploring all cases using dfs
def dfs(idx, sum):
    global answer_max, answer_min, N
    if idx == N:
        answer_max = max(answer_max, sum)
        answer_min = min(answer_min, sum)
        return 
    num = num_list[idx]

    if operator[0]:
        operator[0] -= 1
        dfs(idx+1, sum+num)
        operator[0] += 1

    if operator[1]:
        operator[1] -= 1
        dfs(idx+1, sum-num)
        operator[1] += 1

    if operator[2]:
        operator[2] -= 1
        dfs(idx+1, sum*num)
        operator[2] += 1

    if operator[3]:
        operator[3] -= 1
        # If negative, follow the C++14 criterion
        if sum < 0:
            dfs(idx+1, -((-sum)//num))
        else:
            dfs(idx+1, sum//num)
        operator[3] += 1

dfs(1, num_list[0])
print(answer_max)
print(answer_min)

# Language        : Python3
# Memory          : 30864 KB
# Time            : 104 ms
# Time complexity : O(4^(N-1)) ?