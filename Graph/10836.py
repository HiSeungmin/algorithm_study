# 10836 여왕벌

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(S,pre):
    global ans
    check=0
    for i in Tree[S]:
        if i!=pre:
            check=max(check,dfs(i,S)) 
    if check>=D: 
        ans+=1
    return check+1

N,S,D=map(int,input().split())
Tree=[ [] for _ in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().split())
    Tree[a].append(b)
    Tree[b].append(a)

ans=0
dfs(S,0)
print(2*(ans-1) if ans else 0)