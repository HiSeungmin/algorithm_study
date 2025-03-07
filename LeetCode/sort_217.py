# Contains Duplicate
def containsDuplicate(nums):
    a = set()
    for x in nums:
        if x in a:
            return True
        else:
            a.add(x)
    
    return False
    
print(containsDuplicate([1,2,3,1]))