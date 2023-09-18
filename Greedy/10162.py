# 10162 : 전자레인지

T = int(input())

arr = [ 300, 60, 10]
res = []
cnt = 0

for sec in arr:
    res.append(T//sec)
    T %= sec


if T!=0:
    print(-1)
    exit(0)

for r in res: 
    print(r, end=" ")