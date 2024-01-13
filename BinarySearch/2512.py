# 2512 : 예산
N = int(input())
arr = list(map(int, input().split(' ')))
M = int(input())
arr.sort()

def budget_check(k):
    sum = 0
    for i in range(len(arr)):
        if k>=arr[i]:
            sum += arr[i]
        else:
            sum += k
    return sum

left, right, mid = 0, M, 0
chk = 0
result = 0
while left <= right:
    mid = (left + right) // 2
    chk = budget_check(mid)
    if chk > M or mid > arr[-1]:
        right = mid - 1
    elif chk <= M:
        left = mid + 1
        if result < mid:
            result = mid

print(result)