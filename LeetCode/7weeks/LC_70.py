a = int(input())

def solution(a):
    dp = []
    dp.append(1)
    dp.append(2)
    dp.append(3)

    for i in range(3,45):
        dp.append(dp[i-1]+dp[i-2])
        
    
    return dp[a-1]
        
    
print(solution(a))