import sys
input = sys.stdin.readline

n = int(input())
files = []

for _ in range(n):
    files.append(input())

d = dict()
for file in files:
    format = file.split('.')[1]
    if format not in d.keys():
        d[format] = 1
    else:
        d[format] += 1
    
arr = list(d.keys())
arr.sort()

for i in arr:
    print(i, d[i])