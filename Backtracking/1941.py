#1941 : 소문난 칠공주
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(a,b):
    q = deque()
    q.append([a,b])
    w = [[0]*5 for _ in range(5)]
    cnt = 1
    while q:
        x, y = q.popleft()
        w[x][y] = 1

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<5 and 0<=ny<5 and v[nx][ny] == 1 and w[nx][ny] == 0:
                 w[nx][ny] = 1
                 cnt +=1
                 q.append([nx,ny])
    
    if cnt == 7:
        return True
    else:
        return False

def check():
    for i in range(5):
        for j in range(5):
            if v[i][j] == 1:
                return bfs(i,j)    

def dfs(n, cnt, sCnt):
    global ans
    if cnt > 7:
        return 
    
    if n==25:
        if cnt==7 and sCnt>=4:
            #인접 체크 (모두 인접 시 정답+1)
            if check():
                ans+=1
        return
    
    v[n//5][n%5] = 1   #포함
    dfs(n+1, cnt+1, sCnt + int(arr[n//5][n%5]=='S'))
    v[n//5][n%5] = 0 
    
    dfs(n+1, cnt, sCnt) #포함X

arr = [input() for _ in range(5)]
# 학생번호(0~24), 포함학생수, 다솜파학생수
ans = 0
v = [[0]*5 for _ in range(5)]
dfs(0,0,0)
print(ans)