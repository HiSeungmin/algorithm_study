#1789 : 수들의 합

S = int(input())
cnt = 0
sum = 0

while sum <= S:
    cnt += 1
    sum += cnt

print(cnt-1)