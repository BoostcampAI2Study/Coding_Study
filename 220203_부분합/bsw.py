N, S = map(int, input().split())
nums = list(map(int, input().split()))

nums.append(0)
l,r = 0, 0
ans = 1e9
sum_ = nums[0]
while l<=r and r<N:
    
    if sum_ < S:
        r+=1
        sum_ += nums[r]
    elif sum_ >= S:
        sum_ -= nums[l]
        ans = min(ans, r-l +1)
        l+=1
    

if ans == 1e9:
    print(0)
else:
    print(ans)
