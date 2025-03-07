num = int(input())
s = set()
for _ in range(num):
    s.add(input())

str = list(s)
str.sort()
str.sort(key=len)


for i in str:
    print(i)