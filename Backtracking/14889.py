#14889 : 스타트와 링크
# 방법 1)
def dfs(n,s):
    global ans
    if n == (N//2):
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if v[i] and v[j]: # i, j 모두 방문한거라면
                    start += arr[i][j] # start 팀에 배정
                elif not v[i] and not v[j]: # i, j 모두 방문하지 않으면
                    link += arr[i][j] # 링크 팀에 배정
        ans = min(ans, abs(start-link))
        return
    
    for k in range(s,N):
        if v[k] == 0:
            v[k] = 1
            dfs(n+1,k+1)
            v[k] = 0

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
v = [0]*N
ans = 1e9
dfs(0,0)
print(ans)


# 방법2) 조합으로 풀기
# from itertools import combinations
# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N)]
# members = list(range(N))
# ans = 1e9

# for r1 in combinations(members, N//2):
#     start,link = 0,0
#     r2 = list(set(members)-set(r1))
#     for r in combinations(r1,2):
#         start += arr[r[0]][r[1]]
#         start += arr[r[1]][r[0]]
#     for r in combinations(r2,2):
#         link += arr[r[0]][r[1]]
#         link += arr[r[1]][r[0]]
#     ans = min(ans,abs(start-link))

# print(ans)