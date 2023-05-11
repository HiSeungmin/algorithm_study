# 1541 : 잃어버린 괄호
str = input()
if '-' in str and '+' in str:
    str = str.split('-')
    num = []
    for k in range(len(str)):
        if '+' in str[k]:
            m = str[k].split('+')
            new_m = [int(x) for x in m]
            s = sum(new_m)
            num.append(s)
        else:
            num.append(str[k])
    intList = [int(x) for x in num]
    ans = intList[0]
    for i in range (1, len(intList)):
        ans -= intList[i]
    print(ans)
elif '-' in str:
    str = str.split('-')
    intList = [int(x) for x in str]
    ans = intList[0]
    for i in range (1, len(intList)):
        ans -= intList[i]
    print(ans)
elif '+' in str:
    str = str.split('+')
    intList = [int(x) for x in str]
    print(sum(intList))
else:
    print(str)