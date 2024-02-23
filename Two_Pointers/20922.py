# 20922 겹치는 건 싫어

N, K = map(int, input().split())
lst = list(map(int, input().split()))
left = 0
right = 0
chk = [0]*(max(lst)+1)
ret = 0

while right<N:
    if chk[lst[right]]<K:
        chk[lst[right]]+=1
        right += 1
    else:
        chk[lst[left]]-=1
        left+=1
    ret = max(ret,right-left)
print(ret)
