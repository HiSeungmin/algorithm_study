#19583 싸이버개강총회

S, E, Q = input().split()
s = int(S.split(':')[0]+S.split(':')[1])
e = int(E.split(':')[0]+E.split(':')[1])
q = int(Q.split(':')[0]+Q.split(':')[1])

chat = []
mem = set()
while True:
    try:
        A, B = input().split()
        a = int(A.split(':')[0]+A.split(':')[1])
        chat.append([a,B])
    except:
        break

req = set()
cnt = 0
for i in range(len(chat)):
    if chat[i][0]<=s:
        req.add(chat[i][1])
    if e<=chat[i][0]<=q and chat[i][1] in req:
        req.remove(chat[i][1])
        cnt +=1

print(cnt)

