def dfs(n, lst):
    if n==M:
        print(*lst)
        return
    
    
    for k in range(1, N+1):
        if v[k] == 0 and N-k+2>=M:
            if len(lst)>0 and lst[-1] > (n+1):
                continue
            else:
                v[k] = 1
                dfs(n+1,lst+[k])
                v[k] = 0
        

N, M = map(int, input().split())
v = [0] * (N+1)
dfs(0,[])