import sys
input = sys.stdin.readline

N, M = map(int, input().split())
miro = [ list(map(int,input().split())) for _ in range(N)]
ret  = [[0]*M for _ in range(N)]
ret[0][0] = miro[0][0]

for i in range(N):
    for j in range(M):
        a=0
        b=0
        c=0
        if 0<=i-1<N and 0<=j<M: a=ret[i-1][j]
        if 0<=i<N and 0<=j-1<M: b=ret[i][j-1]
        if 0<=i-1<N and 0<=j-1<M: c=ret[i-1][j-1]
        ret[i][j] = miro[i][j]+max(a,b,c)

print(ret[N-1][M-1])
