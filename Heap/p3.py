#이중우선순위 큐
from collections import deque

def solution(operations):
    answer = [0, 0]
    arr = deque()
    
    for str in operations:
        q = list(arr)
        if str == "D -1" and len(arr)>0:
            arr.popleft()
        elif str == "D 1" and len(arr)>0:
            arr.pop()
        elif "I" in str:
            num = str.split(" ")[1]
            q.append(int(num))
            q.sort()
            arr = deque(q)
    if arr:
        answer[0] = max(arr)
        answer[1] = min(arr)
    return answer

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))