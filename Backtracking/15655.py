# 15655 : N과 M(6)

# def dfs(n, lst):
#     if n == N:
#         if len(lst) == M:
#             print(*lst)
#         return
    
#     dfs(n+1,lst+[arr[n]])
#     dfs(n+1,lst)

# N, M = map(int, input().split())
# arr = list(map(int,input().split()))
# arr.sort()
# dfs(0,[])

def dfs(n, s, lst):
    if n==M:
        print(*lst)
        return
    
    for k in range(s,N):
        dfs(n+1,k+1,lst+[arr[k]])

N, M = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()
dfs(0,0,[])