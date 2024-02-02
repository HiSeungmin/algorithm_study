# 1107 리모콘

import sys
input = sys.stdin.readline
target = int(input())
n = int(input())
broken = list(map(int, input().split()))

min_count = abs(100 - target)
for nums in range(1000001): # 수빈이가 이동하려는 채널의 범위는 500,000 이하지만 채널 자체는 무한대이다.
                            # target보다 작은 값은 물론 큰 값도 찾아줘야하기 때문에 500,000 이상도 가능하다는 점
    nums = str(nums)    
    for j in range(len(nums)):
        if int(nums[j]) in broken:
            break
        elif j == len(nums) - 1:
            min_count = min(min_count, abs(int(nums)-target)+len(nums))

print(min_count)