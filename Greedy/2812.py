#2812 : 크게 만들기

a, b = map(int, input().split())
str = input()
arr = []
cnt = 0

for num in str:
    while arr and arr[-1] < num and cnt!=b:
        arr.pop()
        cnt += 1
    arr.append(num)

if b > cnt:
    cnt -= b
    print(''.join(arr[:cnt]))
else:
    print(''.join(arr))
