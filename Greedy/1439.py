# 1439 : 뒤집기

str = input()
cnt = 0
for k in range(len(str)-1):
    if str[k] != str[k+1]:
        cnt += 1

print((cnt+1)//2)