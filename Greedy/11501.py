#11501 : 주식

n = int(input())

def go():
    m = int(input())
    arr = list(map(int,input().split()))
    arr.reverse()
    sum = 0
    max = arr[0]
    for k in range(1, m):
        if max >= arr[k]:
            sum += (max-arr[k])
        else:
            max = arr[k]

    return sum

    
for _ in range(n):
    print(go())