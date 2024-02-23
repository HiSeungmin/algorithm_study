#11503 가장 긴 증가하는 부분 수열

import sys

N = int(sys.stdin.readline())
A = list(map(int, input().split()))
dp = [1] * N

for i in range(1, N) :
    for j in range(i) :
        if A[i] > A[j] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

# N = int(input())
# A = list(map(int, input().split(' ')))
# output_list = [0]

# for case in A:
#     if output_list[-1] < case:
#         output_list.append(case)
#     else:
#         left = 0
#         right = len(output_list)

#         while left < right:
#             mid = (left + right) // 2
#             if output_list[mid] < case:
#                 left = mid + 1
#             else:
#                 right = mid
#         output_list[right] = case

# print(len(output_list) - 1)