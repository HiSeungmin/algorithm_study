# 1080 : 행렬

dx = [0, 1, 2]
dy = [0, 1, 2]

def dfs(arr, i, j):
    x, y = i, j
    brr = arr

    for k in range(3):
        for e in range(3):
            
            if 0<=x+k<n and 0<=y+e<m:
                arr[x+k][y+e] = 1-arr[x+k][y+e]
 

n,m = map(int, input().split())

arr = []
res = []
for _ in range(n):
    arr.append(list(map(int, input())))

for _ in range(n):
    res.append(list(map(int, input())))

cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] != res[i][j]:
            dfs(arr, i, j)
            cnt += 1


for a in range(n):
    for b in range(m):
        if arr[a][b] != res[a][b]:
            cnt = -1

print(cnt if arr == res else -1)







a,b = map(int,input().split())
count = 0 
    
A = [list(map(int,input())) for _ in range(a)]
B = [list(map(int,input())) for _ in range(a)]

def convert(x,y,A):
    for i in range(x,x+3):
        for j in range(y,y+3):
            A[i][j] = 1-A[i][j]

for i in range(a-2):
    for j in range(b-2):
        if A[i][j] != B[i][j]:
            convert(i,j,A)
            count +=1

flag = True
for i in range(a):
    for j in range(b):
        if A[i][j] != B[i][j]:
            flag = False
            break
            
print(count) if flag==True else print(-1)