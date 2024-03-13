# 15900 나무 탈출

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**5)

# n = int(input())

# answer = 0
# graph = [[] for _ in range(n+1)]
# visited = [0 for _ in range(n+1)]
# distance = [0 for _ in range(n+1)]

# for i in range(n-1):
#     x, y = map(int, input().rstrip().split())
#     graph[x].append(y)
#     graph[y].append(x)

# def dfs(x):
#     visited[x] = 1
#     for k in graph[x]:
#         if visited[k] == 0:
#             distance[k] = distance[x] + 1 
#             dfs(k)
#     return 0

# dfs(1)

# for i in range(2,n+1):
#     if len(graph[i]) == 1:
#         answer += distance[i]

# if answer % 2 == 0:
#     print("No")
# else:
#     print("Yes")



import sys
N = int(input())
arr = [[] for _ in range(N+1)]
for i in range(N-1):
    n1, n2 = map(int, sys.stdin.readline().rstrip().split())
    arr[n1].append(n2)
    arr[n2].append(n1)

stack = [[1, 0]]
chk = [0] * (N+1)
chk[1] = -1
ls = []

while stack:
    cn, l = stack.pop()
    chk[cn] = 1

    if cn != 1 and len(arr[cn]) == 1:
        ls.append(l)
        continue

    for nn in arr[cn]:
        if chk[nn] == 0:
            stack.append([nn, l+1])

sum_ls = sum(ls)

if sum_ls % 2:
    print('Yes')
else:
    print('No')