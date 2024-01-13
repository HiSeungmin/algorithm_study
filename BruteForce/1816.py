#1816 : 암호 키

n = int(input())

for _ in range(n):
    num = int(input())

    for k in range(2,1000001):
        if num%k==0:
            print("NO")
            break
        if k==1000000:
            print("YES")
            break