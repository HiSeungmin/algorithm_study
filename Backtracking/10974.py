#10974 : 모든 순열

def dfs(n,lst):
    if n==N:
        print(*lst)
    
    for k in range(1, N+1):
        if v[k]==0:
            v[k] = 1
            dfs(n+1,lst+[k])
            v[k] = 0

N = int(input())
v=[0]*(N+1)
dfs(0,[])