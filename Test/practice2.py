import sys
input = sys.stdin.readline

N, S = map(int,input().split())
arr = list(map(int,input().split()))

len = N+1
end = 0
sum = 0
for start in range(N):
    while sum < S and end<N:
        sum += arr[end]
        end += 1
        
    if sum >= S:
        len = min(end - start,len)
    
    sum -= arr[start] 

if len == N+1:
    print(0)
else:
    print(len)