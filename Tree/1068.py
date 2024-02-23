#1068 : 트리
import sys
input = sys.stdin.readline

def dfs(k, arr):
    arr[k] = -2
    for i in range(len(arr)):
        if arr[i] == k:
            dfs(i, arr)

N = int(input())
arr = list(map(int,input().split()))
K = int(input())

dfs(K,arr)

cnt = 0
for r in range(len(arr)):
    if arr[r] != -2 and r not in arr:
        cnt += 1

print(cnt)