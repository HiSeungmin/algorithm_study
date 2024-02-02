# 9625 BABBA

lst = []
lst.append([1,0])
lst.append([0,1])

def dp(n):
    for i in range(2,n+1):
        a = lst[i-1][0]+lst[i-2][0]
        b = lst[i-1][1]+lst[i-2][1]
        lst.append([a,b])

K = int(input())
if K<=1:
    print(*lst[K])
else:
    dp(K)
    print(*lst[K])