# 2133 : 타일 채우기
n = int(input())
d=[0]*(n+1)
d[0] = 1
d[1] = 0
d[2] = 3

def dp(x):
    if d[x]!=0:
        return d[x]
    result = 3*dp(x-2)
    for i in range(3, x+1):
        if i%2==0:
            result += (2*dp(x-i))
    d[x] = result
    return result

print(dp(n))