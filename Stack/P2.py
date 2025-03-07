# 기능 개발
import math
def solution(progresses, speeds):
    t = []
    
    # 첫 번째 작업의 배포 일수를 올바르게 계산
    t.append(math.ceil((100 - progresses[0]) / speeds[0]))
    
    for i in range(1, len(progresses)):
        num = math.ceil((100 - progresses[i]) / speeds[i])  # 배포 일수 올림 적용
        t.append(max(num, t[i-1]))  # 앞의 작업보다 더 오래 걸릴 경우 보정

    result = []
    num = 1
    for i in range(len(t) - 1):
        if t[i] != t[i + 1]:
            result.append(num)
            num = 1
        else:
            num += 1
    result.append(num)   
    return result  

print(solution([93, 30, 55], [1, 30, 5]))  # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))  # [1, 3, 2]
print(solution([20, 99, 93, 30, 55, 10], [5, 10, 1, 1, 30, 5]))  # [3, 3]


