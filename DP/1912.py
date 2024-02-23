#1912 연속합

N = int(input())
arr = list(map(int,input().split()))
ret = [0]*N
ret[0] = arr[0]
for i in range(1,N):
    if ret[i-1]+arr[i]>arr[i]:
        ret[i] = ret[i-1]+arr[i]
    else:
        ret[i] = arr[i]

print(max(ret))
