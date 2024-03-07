# 1339 : 단어 수학

num = int(input())
arr = []
for _ in range(num):
    arr.append(input())
alphabet = [0 for _ in range(26)]
for str in arr:
    str=str[::-1] # 거꾸로 출력
    len = 1
    for s in str:
        index = ord(s) # ord() : 아스키코드로 변환
        alphabet[index-65] += len
        len *= 10

alphabet.sort()
alphabet.reverse()

sum = 0
m = 9
for k in alphabet:
    if k == 0:
        break
    sum += (k*m)
    m -= 1
print(sum)