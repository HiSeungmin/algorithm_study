#2839 : 설탕 배달

N = int(input())

i = 1
min = 5000

while i <= (N//5):
    if (N-(5*i))%3 == 0:
        num = 0
        num += i
        num += (N-(5*i))//3
    i += 1

if num == 0 and num%3==0:
    num = N//3

if num == 0:
    print(-1)
else: 
    print(num)