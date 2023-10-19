#2012 : 등수 매기기

n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()
cnt = 0
for k in range(n):
    cnt += abs((k+1)-arr[k])

print(cnt)