#15650 : N과 M(2)

# 방법 1)
def dfs(n, lst):
    if n>N:
        if len(lst) == M:
            print(*lst)
        return
    
    dfs(n+1, lst+[n])
    dfs(n+1, lst)
    
N, M = map(int, input().split())
dfs(1,[])


# 방법 2)
# def dfs(n, s, lst):
#     if n==M:
#         print(*lst)
#         return
    
#     for k in range(s,N+1):
#         dfs(n+1,k+1,lst+[k])

# N, M = map(int, input().split())
# v = [0] * (N+1)
# dfs(0,1,[])
