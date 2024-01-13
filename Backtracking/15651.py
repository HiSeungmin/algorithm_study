#15651 : N과 M(3)
def dfs(n, lst):
    if n == M:
        print(*lst)
        return

    dfs(n+1,lst+[n])

N, M = map(int, input().split())
dfs(0,[])