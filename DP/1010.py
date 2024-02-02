# 1010 다리 놓기
def fac(n):
    ret = 1
    for k in range(1,n+1):
        ret *= k  
    return(ret)

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    bridge = fac(b) // (fac(b-a)*fac(a))
    print(bridge)