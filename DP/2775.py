# 2775
T = int(input())

for i in range(T):
    K = int(input())
    N = int(input())
    apt = [[0]*(N+1) for _ in range(K+1)]

    for i in range(N+1):
        apt[0][i] = i
    
    for i in range(1,K+1):
        for j in range(N+1):
            apt[i][j] = sum(apt[i-1][:j+1])

    print(apt[K][N])
            