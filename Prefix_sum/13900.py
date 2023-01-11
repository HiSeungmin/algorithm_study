# 13900 : 순서쌍의 곱의 합
import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
ans = 0
s = sum(arr)
# for i in range(0, N):
#     s += arr[i]

arr.reverse()
for k in reversed(range(N)):
    a = arr.pop()
    s -= a
    ans += a*s

print(ans)