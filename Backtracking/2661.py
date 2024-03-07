# 2661 좋은 수열

import sys
input = sys.stdin.readline

def dfs(idx):
    for i in range(1, (idx//2)+1):
        if s[-i:] == s[-2*i:-i]: 
            return -1

    if idx == N:
        for i in range(N): 
            print(s[i], end = '')
        return 0

    for i in range(1, 4):
        s.append(i)
        if dfs(idx + 1) == 0:
            return 0
        s.pop()

N = int(input())
s = []
dfs(0)