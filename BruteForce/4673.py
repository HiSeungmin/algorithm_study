# 4673 : 셀프넘버

num = set(range(1,10001))
g_num = set()

for k in range(1,10001):
    for j in str(k):
        k+= int(j)
    g_num.add(k)

self_num = sorted(num-g_num)
for i in self_num:
    print(i)