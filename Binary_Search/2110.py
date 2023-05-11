# 2110 : 공유기 설치
N, C = map(int, input().split(' '))
home = []
for _ in range(N):
    home.append(int(input()))
home.sort()

left, right = 1, home[-1] - home[0]
result = 0

while left <= right:
    mid = (left + right) // 2
    current = home[0]
    cnt = 1

    for i in range(1, len(home)):
        if home[i] >= current + mid:
            cnt += 1
            current = home[i]
    if cnt >= C:
        left = mid + 1
        result = mid
    else:
        right = mid -1

print(result)