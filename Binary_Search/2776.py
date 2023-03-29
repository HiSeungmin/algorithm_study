# 2776 : 암기왕
T = int(input())
for _ in range(T):
    a = int(input())
    arr1 = list(map(int, input().split()))
    a = int(input())
    arr2 = list(map(int, input().split()))
    ans = [0 for _ in range(len(arr2))]
    arr1.sort()
    for i in range(len(arr2)):
        left = 0
        right = len(arr1) - 1
        while left <= right:
            mid = (left + right)//2
            if arr1[mid] == arr2[i]:
                ans[i] = 1
                break
            elif arr1[mid] > arr2[i]:
                right = mid-1
            else:
                left = mid + 1
    for i in ans:
        print(i)