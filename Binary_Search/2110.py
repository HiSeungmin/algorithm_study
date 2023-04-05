# 2110 : 공유기 설치

N, C = map(int, input().split(' '))
home = []
for _ in range(N):
    home.append(int(input()))
home.sort()

def check(m):
    pass

left, right, mid = 0, N, 0

while left<=right:
    mid = (left+right) // 2
    chk = check(mid)