# 같은 숫자는 싫어

def solution(arr):
    result = []
    
    for i in arr:
        if len(result) == 0 or result[-1] != i:
            result.append(i)
    
    return result


print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3]))

# 채점 결과
# 정확성: 71.9
# 효율성: 28.1
# 합계: 100.0 / 100.0