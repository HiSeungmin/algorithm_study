#14568 : 2017 연세대학교 프로그래밍 경시대회

n = int(input())

ans = 0

for a in range(1, n+1):
    for b in range(1, n+1):
        for c in range(1, n+1):
            if(a+b+c == n):
                if(c>=b+2):
                    if(a%2==0):
                        ans +=1

print(ans)