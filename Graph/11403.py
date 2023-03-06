# 11403 경로 찾기

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))
    
for k in range(0, N):         # 경유지 노드
    for i in range(0, N):     # 출발 노드
        for j in range(0, N): # 도착 노드
            if arr[i][k]==1 and arr[k][j]==1:
                arr[i][j] = 1

for li in arr:
    for el in li:
        print(el, end =" ")
    print()
