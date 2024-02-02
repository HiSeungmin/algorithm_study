#13023 ABCDE

def dfs(n,idx):
    global ans
    if idx==4: #사람 수가 최소 5명이기때문에 4개가 성립되면 무조건 1
        ans = 1
        return
    
    for k in frnd[n]:
        if v[k] == 0:
            v[k] = 1
            dfs(k, idx+1)
            v[k] = 0

N, M = map(int, input().split())
frnd = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    frnd[a].append(b)
    frnd[b].append(a)

ans = 0
v=[0]*N
for i in range(N):
    v[i] = 1
    dfs(i,0)
    v[i] = 0

print(ans)