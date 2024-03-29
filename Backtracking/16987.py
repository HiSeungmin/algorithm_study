# 16987 : 계란으로 계란치기

def dfs(n,cnt):
    global ans

    if ans >=(cnt+(N-n)*2):return

    if n == N:
        ans = max(ans,cnt)
        return
    
    if arr[n][0]<=0:
        dfs(n+1,cnt)
    else:
        flag = False # 한번도 안 부딪혔어도 다음 단계로 고
        for k in range(0,N):
            if n==k or arr[k][0] <= 0: continue
            flag = True
            arr[n][0] -= arr[k][1]
            arr[k][0] -= arr[n][1]
            dfs(n+1, cnt+int(arr[n][0]<=0)+int(arr[k][0]<=0))
            arr[n][0] += arr[k][1]
            arr[k][0] += arr[n][1]
        
        if flag == False:
            dfs(n+1, cnt)

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = 0
dfs(0,0)
print(ans)