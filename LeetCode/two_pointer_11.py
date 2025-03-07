# 11. Container With Most Water

def search(height):
    start = 0
    end = len(height)-1
    output = 0
    
    while start < end:
        a = 0
        
        if height[start] <= height[end]:
            a = height[start]*(end-start)
            start += 1
        else:
            a = height[end]*(end-start)
            end -=1
            
        if output < a:
            output = a
            
        
    return output    

height = [1,8,6,2,5,4,8,3,7]
print(search(height))