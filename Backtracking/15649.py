#15649 N과 M(1)

def dfs(n, lst):
    # 종료조건(n에 관련) 처리 + 정답 처리
    if n==M:
        print(*lst)
        #ans.append(lst)
        return
    
    for j in range(1, N+1):
        if v[j]==0:
            v[j]=1
            dfs(n+1, lst+[j])
            v[j]=0

N, M = map(int, input().split())
ans = []
v = [0]*(N+1)

dfs(0, [])
# for lst in ans:
#     print(*lst)
