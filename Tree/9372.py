# 9372 : 상근이의 여행 (신장 트리)

def dfs(x, cnt):
    checked[x] = 1
    for i in city[x]:
        if checked[i] == 0:
            cnt = dfs(i, cnt+1)
    
    return cnt

T = int(input())

while T:
    N, M = map(int, input().split())

    city = [[] for _ in range(N+1)]
    checked = [0 for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        city[a].append(b)
        city[b].append(a)
    
    print(dfs(1, 0))
    
    T-=1