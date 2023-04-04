# 17266 : 어두운 굴다리

N = int(input())
M = int(input())
arr = []
if M > 1:
    arr = list(map(int, input().split(' ')))
else:
    arr.append(int(input()))

def bright_check(k):
    check = True
    for i in range(len(arr)-1):
        l = arr[i] + k
        r = arr[i+1] - k
        if (l - r):
            check = False
    if arr[0] - k > 0 or arr[-1] + k < N:
        check = False
    return check 

left, right, mid = 0, N, 0
result = 0
chk = False

while left <= right:
    mid = (left+right) // 2
    chk = bright_check(mid)
    if chk:
        right = mid -1
        if result > mid:
            result = mid
    else:
        left = mid+1

print(result)