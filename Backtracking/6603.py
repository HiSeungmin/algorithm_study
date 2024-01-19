# 6603 : 로또
def dfs(n,s,lst):
    if n == 6:
        print(*lst)
        return
    
    for k in range(s,idx+1):
        if v[k] == 0:
            v[k]=1
            dfs(n+1,k,lst+[arr[k]])
            v[k] =0

idx = 1
while idx != 0:
    arr = list(map(int,input().split()))
    idx = arr[0]
    v = [0]*(idx+1)
    dfs(0,1,[])
    print()
