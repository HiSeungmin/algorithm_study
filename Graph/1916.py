# 1916 : 최소비용 구하기

N = int(input())
M = int(input())

cities = [[] for _ in range(M+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    cities