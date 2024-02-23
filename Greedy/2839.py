#2839 : 설탕 배달

N = int(input())

i = 0
cnt = 0
while 1:
    a = N-((N//5)*5)+(5*i)

    if a%3 == 0:
        cnt += (N//5)-i
        print(cnt+(a//3))
        exit(0)
    i+=1
    if (5*i)>N:
        break

if a%3==0: print(a//3)
else: print(-1)