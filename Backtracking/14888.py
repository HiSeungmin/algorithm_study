#14888 : 연산자 끼워넣기

def operator(a,b,x):
    ret = 0
    if x == '+':
        ret = (a+b)
    elif x == '-':
        ret = (a-b)
    elif x == '*':
        ret = (a*b)
    elif x == '/':
        if a<0 or b<0:
            ret= (abs(a)//abs(b))*(-1)
        else:
            ret = a//b
    
    return ret

def dfs(n, sum):
    global maxRet, minRet
    if n == (N-1):
        maxRet = max(maxRet, sum)
        minRet = min(minRet, sum)
        return

    for k in range(N-1):
        if v[k] == 0:
            v[k] = 1
            dfs(n+1, operator(sum,num[n+1],ope[k]))
            v[k] = 0


N = int(input())
num = list(map(int,input().split()))
op = list(map(int,input().split()))
strg = '+'*op[0]+'-'*op[1]+'*'*op[2]+'/'*op[3]
ope = list(strg)
maxRet = -1*(10**9)
minRet = 10**9+1
v = [0]*(N-1)
dfs(0,num[0])
print(maxRet)
print(minRet)