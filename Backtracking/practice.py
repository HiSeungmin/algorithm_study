
def dfs(n, cnt):
    global ans
    if n == N:
        ans = max(ans, cnt)
        return
    
    if arr[n][0] <= 0:
        dfs(n+1, cnt)
    else:
        flag = False
        for k in range(N):
            if n==k or arr[k][0]<=0:
                continue
            flag = True
            arr[n][0] -= arr[k][1]
            arr[k][0] -= arr[n][1]
            dfs(n+1, cnt+int(arr[n][0]<=0)+int(arr[k][0]<=0))
            arr[n][0] -= arr[k][1]
            arr[k][0] -= arr[n][1]
        if flag == False:
            dfs(n+1, cnt)


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = 0
dfs(0,0)
print(ans)