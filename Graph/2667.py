# 2667 : 단지번호 붙이기
#import sys
from collections import deque
#input = sys.stdin.readline
arr = []
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

check = deque([[0,0]])
dx = [0, 0, -1 , 1]
dy = [-1, 1, 0, 0]
