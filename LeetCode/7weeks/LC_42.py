# Trapping Rain Water

# def solution(height):
#     start = 0
#     end = 0
#     result = 0
#     num = 0
#     while end < len(height):
#         if height[start] <= height[end]:
#             print(num)
#             result += num
#             num = 0
#             start = end
#             end += 1
#         else: 
#             num += height[start]-height[end]
#             end += 1
#     return result


# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# print(solution(height))


def trap(height):
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += max(0, left_max - height[left]) 
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += max(0, right_max - height[right])

    return water

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height)) 
