#15664 : N과 M(10)

def dfs(n, s, lst):
    if n == M:
        print(*lst)
        return
    
    prev = 0

    for k in range(s,N):
        if v[k]==0 and prev!=arr[k]:
            v[k]=1
            prev = arr[k]
            dfs(n+1,k+1,lst+[arr[k]])
            v[k]=0


N, M = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()
v=[0]*N
dfs(0,0,[])