k = int(input())

arr = list(input().split())

ans = []
def dfs(level, st):
    if level == k+1:
        ans.append(st)
        return
    else:
        for i in range(10):
            if level == 0:
                dfs(level+1, st+str(i))
            else:
                if arr[level-1] == '<' and int(st[-1]) < i and not str(i) in st:
                    dfs(level+1, st+str(i))
                if arr[level-1] == '>' and int(st[-1]) > i and not str(i) in st:
                    dfs(level+1, st+str(i))

dfs(0,"")
ans.sort()

print(ans[-1])
print(ans[0])
