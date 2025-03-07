# Valid Parentheses

def solution(s):
    a = list()
    
    for i in s:
        if i in ["(","[","{"]:
            a.append(i)
        elif i == ")":
            if a[-1] != "(":
                return False
            else:
                a.pop()
        elif i == "]":
            if a[-1] != "[":
                return False
            else:
                a.pop()
        elif i == "}":
            if a[-1] != "{":
                return False
            else:
                a.pop()
    return len(a)==0

s = input()
print(solution(s))