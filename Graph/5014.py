# 5014 : 스타트링크
from collections import deque
def bfs():
    que = deque()
    que.append(S)
    dist[S] = 0
    while que:
        x = que.popleft()
        if x == G:
            print(dist[x])
            break
        for nx in (x+U, x-D):
            if 0<nx<=F and dist[nx] == -1:
                dist[nx] = dist[x]+1
                que.append(nx)
    if x !=G:
        print("use the stairs")
        
F, S, G, U, D = map(int, input().split(' '))
dist = [-1 for _ in range(F+1)]
bfs()