import sys
from queue import deque
input = sys.stdin.readline

N = int(input())
a = [i+1 for i in range(N)]
arr = deque(a)
for i in range(N-1):
    arr.popleft()
    b = arr.popleft()
    arr.append(b)

print(arr[-1])