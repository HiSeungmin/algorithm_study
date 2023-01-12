# 10986 : 나머지 합
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum = 0
num = [0] * M

for i in range(N):
  sum += arr[i]
  num[sum % M] += 1

result = num[0]

# 나머지가 같은 구간 두 개 뽑기, iC2
for i in num:
  result += i*(i-1)//2

print(result) 