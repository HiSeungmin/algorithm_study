#26364 부동산 다툼
import sys
input = sys.stdin.readline

N, Q = map(int,input().split())
v = [0]*(N+1)

for _ in range(Q):
    i = int(input())
    target = i
    flag = 0

    while target:

        if v[target] !=0:
            flag = target
        target //=2        

    if flag:
        print(flag)
    else:
        v[i] = 1
        print(0)