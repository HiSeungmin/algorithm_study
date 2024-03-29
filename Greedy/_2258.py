#2258 : 정육점

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = []

for _ in range(N):
    a, b = map(int, input().split())
    arr.append((b, a))
arr = sorted(arr, key=lambda x: (x[0], -x[1]))
print(arr)
ans = sys.maxsize
weight, same = 0, 0
flag = False

for i in range(N):
    weight += arr[i][1]
    if i >= 1 and arr[i][0] == arr[i - 1][0]:
        same += arr[i][0]
    else:
        same = 0
    if weight >= M:
        ans = min(ans, arr[i][0] + same)
        flag = True
print(ans if flag else -1)