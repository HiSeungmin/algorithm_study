#2785:체인

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
cnt = 0

if arr[0] >= n:
    print(n-1)
    exit(0)

cnt = 0
for i in range(n):
    cnt += arr[i]

    a = n-(i+1)
    if cnt < a:
        continue

    if cnt >= a:
        print(a)
        exit(0)