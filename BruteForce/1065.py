#1065 한수
N = int(input())
cnt = 99

if N < 100:
    print(N)
    exit()

for k in range(100,N+1):
    a1 = k//100
    a2 = (k-a1*100)//10
    a3 = (k-a1*100-a2*10)
    if abs(a1-a2) == abs(a2-a3):
        if (a1<=a2 and a2 <=a3) or (a1>a2 and a2>a3):
            cnt+=1

print(cnt)