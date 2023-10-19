#1449 : 수리공 항승

N, L = map(int, input().split())
arr  = list(map(int, input().split()))

arr.sort()

tape = 1
gap = 0
cnt = 0
for t in range(1,N):
    gap = arr[t] - arr[t-1]
    if gap+tape <= L:
        tape += gap
    else:
        tape = 1
        cnt += 1
    
if tape > 0: print(cnt+1)
else: print(cnt)