N = int(input())
lst = list(map(int,input().split()))
X = int(input())

lst.sort()
start, end = 0, N-1
cnt = 0
while start<end:
    if lst[start]+lst[end] > X:
        end -= 1
    elif lst[start]+lst[end] < X:
        start += 1
    elif lst[start]+lst[end] == X and start!= end:
        cnt += 1
        end -= 1
        start += 1

print(cnt)