# 15665 : N과 M(11)

# def dfs(n,lst):
#     if n == M:
#         print(*lst)
#         return
    
#     prev = 0
#     for k in range(N):
#         if prev!=arr[k]:
#             prev = arr[k]
#             dfs(n+1,lst+[arr[k]])
            
# N, M = map(int, input().split())
# arr = list(map(int,input().split()))
# arr.sort()

# dfs(0,[])

# 15665 : N과 M(12)
def dfs(n,s, lst):
    if n == M:
        print(*lst)
        return
    
    prev = 0
    for k in range(s,N):
        if prev!=arr[k]:
            prev = arr[k]
            dfs(n+1,k,lst+[arr[k]])
            
N, M = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()

dfs(0,0,[])