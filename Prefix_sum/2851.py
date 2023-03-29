# 2851 : 슈퍼 마리오
p = 100
sum = 0
result = 0
for _ in range(10):
    A = int(input())
    sum += A
    if sum == 100:
        result = 100
    if result!=100 and abs(100-sum)<p:
        p = abs(100-sum)
        result = sum
    elif result!=100 and abs(100-sum) == p:
        result = sum
    
print(result)