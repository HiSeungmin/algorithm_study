#12018 : 연세 토토

n, m = map(int, input().split())
res = 0
c = []

for i in range(n):
    p, l = map(int, input().split())
    point = list(map(int, input().split()))
    point.sort(reverse=True)
    if p < l:
        c.append(1)
    else:
        mile = point[l - 1]
        c.append(mile)

c.sort()
for class_m in c:
    if m - class_m >= 0:
        res += 1
        m -= class_m
print(res)