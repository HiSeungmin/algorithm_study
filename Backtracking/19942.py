# 19942 : 다이어트


def dfs(n, lst, cost, p,f,s,v):
    global ans, res
    if n==N:
        if p>=mp and f>=mf and s>=ms and v>=mv:
            if ans > cost:
                ans = cost
                res = lst
            elif ans == cost:
                res = sorted((res,lst))[0]
        return
    dfs(n+1,lst, cost, p,f,s,v) 
    dfs(n+1,lst+[n+1],cost+arr[n][4], p+arr[n][0],f+arr[n][1],s+arr[n][2],v+arr[n][3]) 
    


N = int(input())
mp, mf, ms, mv = map(int,input().split())
arr = [ list(map(int,input().split())) for _ in range(N)]
ans = 1e9+1
res = []
dfs(0, [],0,0,0,0,0)
res.sort()
if ans == 1e9+1:
    print(-1)
else: 
    print(ans)
    print(*res)