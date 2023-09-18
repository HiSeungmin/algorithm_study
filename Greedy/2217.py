# 2217 : 로프

N = int(input())
ropes = []
for _ in range(N):
    ropes.append(int(input()))

ropes.sort()
max = 0
for idx in range(N):
    if max <= ropes[idx]*(N-idx):
        max = ropes[idx]*(N-idx)

print(max)