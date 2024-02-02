# 18429 근손실

def dfs(n, lst, last, wgt,ch):
    global ans
    if n==N:
        if ch == 0:
            ans+=1
        return

    
    for k in range(N):
        if v[k] == 0: 
            v[k] = 1
            dfs(n+1,lst+[kit[k]],last+kit[k]-K,wgt+[last+kit[k]-K],ch+int(ch != 0 or last<500))
            v[k] = 0
        

N, K = map(int, input().split())
kit = list(map(int, input().split()))
v = [0]*N
ans = 0
dfs(0, [],500, [],0)
print(ans)