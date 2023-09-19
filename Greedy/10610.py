# 10610 : 30

three = list(map(int, input()))

s = sum(three)
three.sort(reverse=True)
if three[-1]==0 and s%3==0:
    for i in three:
        print(i, end="")
else:
    print(-1)