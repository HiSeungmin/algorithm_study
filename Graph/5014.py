# 5014 : 스타트링크
F, S, G, U, D = map(int, input().split(' '))
cnt = 0
def bfs():
    c_floor = S
    if c_floor < G:
        c_floor += U
    elif c_floor > G:
        c_floor -= D

    if c_floor <= F:
        cnt += 1
        