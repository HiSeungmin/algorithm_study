# 3020 : 개똥벌레 (이분탐색, 누적합)

N, H = map(int, input().split())
arr = [0]
for _ in range(N):
    arr.append(int(input()))

result = []
for k in range(1, H+1):
    cnt = 0
    for j in range(1, N+1):
        if j%2 != 0:
            if arr[j] >= k:
                cnt += 1
        else:
            if arr[j] > H-k:
                cnt += 1
    result.append(cnt)

#print(result)
print(min(result), end=" ")
print(result.count(min(result)))

left, right, mid = 1, len(arr), 0
while left <= right:
    mid = (left+right) // 2
    