#5555 반지
fStr = input()
N = int(input())
arr = []
for _ in range(N):
    arr.append(input())

def chk(k):
    for i in range(10):
        str1 = arr[k][:i]
        str2 = arr[k][i:]
        tmp = (str2+str1)
        if fStr in tmp:
            return 1
    return 0

cnt = 0
for k in range(N):
    if fStr in arr[k]:
        cnt += 1
    else:
        cnt += chk(k) 

print(cnt)