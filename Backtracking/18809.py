# 18809 : Gaaaaaaaaaarden

from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(tlst):
    q = deque()
    v = [[0]*(M+2) for _ in range(N+2)]
    cnt = 0

# 큐에 초기데이터들 삽입(v표시)
    for k in range(TC):
        if tlst[k] == 0: continue
        ti, tj = lst[k]
        q.append((ti,tj))
        v[ti][tj] = tlst[k]

    while q:
        ci, cj = q.popleft()
        if v[ci][cj] == 25000: continue

        # 네방향, 범위내(X), 미방문, 호수(꽃)이 아니면
        for k in range(4):
            nx = ci + dx[k]
            ny = cj + dy[k]
            
            if arr[nx][ny] == 0 or v[nx][ny] == 25000:
                continue
            
            if v[nx][ny] == 0: #처음 방문
                if v[ci][cj]<0: # R : 1감소
                    v[nx][ny] = v[ci][cj] - 1
                    q.append((nx,ny))
                else: # G : 1증가
                    v[nx][ny] = v[ci][cj]+1
                    q.append((nx,ny))
            else: #  이미 기록 => 꽃을 피울 수 있는지 체크
                if v[ci][cj]<0: # R
                    if (v[nx][ny] + v[ci][cj] - 1) == 0:
                        cnt += 1
                        v[nx][ny] = 25000
                else: # G
                    if (v[nx][ny] + v[ci][cj] + 1) == 0:
                        cnt += 1
                        v[nx][ny] = 25000
    return cnt

def dfs(n, rCnt, gCnt, tlst):
    global ans
    if n == TC: # 모든 땅을 결정했으면 종료
        if rCnt == RC and gCnt == GC:
            ans = max(ans, bfs(tlst))
        return
    
    dfs(n+1, rCnt+1, gCnt, tlst+[-1]) # 빨간색
    dfs(n+1, rCnt, gCnt+1, tlst+[1])  # 초록색
    dfs(n+1, rCnt, gCnt, tlst+[0])    # 안 뿌리는 경우


N, M, RC, GC = map(int, input().split())
arr = [[0]*(M+2)]+[[0]+list(map(int,input().split()))+[0] for _ in range(N)]+[[0]*(M+2)]

lst = []
for i in range(1, N+1):
    for j in range(1, M+1):
        if arr[i][j] == 2: # 배양액 가능한 땅이면 좌표저장
            lst.append((i,j))

TC = len(lst) # 배양 가능한 모든 땅 수

# [1] 가능한 모든 장소에 배양액 뿌리는 방법 순회
ans = 0
dfs(0,0,0,[])
print(ans)