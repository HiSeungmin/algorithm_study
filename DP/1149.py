#1149 RGB거리

N = int(input())
home = [0]*N

for i in range(N):
    home[i] = list(map(int,input().split()))

for k in range(1,N):
    home[k][0] = min(home[k-1][1],home[k-1][2])+home[k][0]
    home[k][1] = min(home[k-1][0],home[k-1][2])+home[k][1]
    home[k][2] = min(home[k-1][0],home[k-1][1])+home[k][2]

print(min(home[N-1][0],home[N-1][1],home[N-1][2]))