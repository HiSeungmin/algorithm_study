# Basic Calculator

def calculate(s):
    stack = []
    num = 0
    sign = 1 
    result = 0
    
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char) # 두 자리 이상 숫자
        elif char in ['+', '-']:
            result += sign * num
            num = 0
            sign = 1 if char == '+' else -1
        elif char == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            result += sign * num
            num = 0
            result *= stack.pop()  
            result += stack.pop()  

    result += sign * num 
    return result


s = "(1+(4+5+2)-3)+(6+8)"
print(calculate(s)) 
