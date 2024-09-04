def stEXE(arr):
    st = []
    for i in arr:
        if i == '(':
          st.append(i)
        elif len(st) > 0:
            st.pop()
        else:
            return "NO"
    
    if len(st) != 0:
        return "NO"    
    else:
        return "YES"
    
N = int(input())

for _ in range(N):
    arr = list(input())
    print(stEXE(arr))
   