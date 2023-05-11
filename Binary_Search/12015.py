# 12015 : 가장 긴 증가하는 부분 수열 2
N = int(input())
A = list(map(int, input().split(' ')))
output_list = [0]
for case in A:
    if output_list[-1] < case:
        output_list.append(case)
    else:
        left = 0
        right = len(output_list)

        while left < right:
            mid = (left + right) // 2
            if output_list[mid] < case:
                left = mid + 1
            else:
                right = mid
        if output_list[-1] < case:
            output_list[right] = case

print(len(output_list) - 1)

# 10
# 100 50 70 90 75 87 105 78 110 60