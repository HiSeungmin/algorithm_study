#1476 : 날짜 계산

E, S, M = map(int, input().split())
ans = 1

while True:
    if (ans-E)%15 == 0 and (ans-S)%28==0 and (ans-M)%19==0:
        print(ans)
        break
    ans += 1