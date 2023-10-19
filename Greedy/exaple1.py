# 1이 될 때까지

n, k = map(int, input().split())
print(n//k)
print((n//k)*k)


result = 0

while True:
    target = (n//k)*k
    result += (n-target)
    n = target  
    print("==>", target, result, n)
    if n<k:
        break
    
    result += 1
    n //= k
    print("-->",result, n)

result += (n-1)
print(result)