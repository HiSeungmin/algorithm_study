#13913 숨바꼭질4
from collections import deque

def path(x):
    arr = []
    temp = x
    for _ in range(v[x]+1):
        arr.append(temp)
        temp = dist[temp]
    arr.reverse()
    print(*arr)

def dfs():
    q = deque()
    q.append(N)

    while q:
        x = q.popleft()
        
        if x == M:
            print(v[M])
            path(x)
            return
        
        for i in (x-1,x+1,2*x):
            if 0<=i<=100000 and v[i] == 0:
                v[i] = v[x]+1
                dist[i] = x
                q.append(i)

N, M = map(int,input().split())
v = [0]*100001
dist = [0]*100001
dfs()
