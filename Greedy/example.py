# 1이 될 때까지

n, k = map(int, input().split())

result = 0

while True:
	# n이 k로 나누어 떨어지는 수가 될 때까지 빼기
	# n을 k로 나누었을 때, 가장 가까운 k로 나누어떨어지는 수를 구할때
    target = (n//k) * k 
    result += ( n - target)
    n = target
    # n이 k보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출    
    if n<k:
        break
    result+=1
    n//=k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)