# 11687 : 팩토리얼 0의 개수

M = int(input())
def find_zero(n):
    zeros = 0
    while n >= 5:
        zeros += n//5
        n //= 5
    return zeros

left, right, mid = 1, M*5, 0
while left <= right:
    mid = (left + right) // 2
    zero_cnt = find_zero(mid)
    if zero_cnt < M:
        left = mid + 1
    else:
        right = mid - 1
        result = mid

if find_zero(result) == M:
    print(result)
else:
    print(-1)