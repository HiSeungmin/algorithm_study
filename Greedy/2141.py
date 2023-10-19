#2141 : 우체국


town = []
allPPL = 0

N = int(input())

for i in range(N):
    n_town, people = map(int, input().split())
    town.append([n_town, people])
    allPPL += people

town.sort(key = lambda x:x[0])

cnt = 0
for i in range(N):
    cnt += town[i][1]
    if cnt >= allPPL/2:
        print (town[i][0])
        break




# 시간초과 코드
# n = int(input())
# arr= []
# for _ in range(n):
#     arr.append(list(map(int, input().split())))

# arr.sort()
# print(arr)
# dist = 1000000000
# ret = 0
# for i in range(n):
#     sum = 0
#     for j in range(n):
#         if i!=j:
#             sum += abs(arr[j][0]-arr[i][0])*arr[j][1]
#     print(arr[i][0],arr[i][1],sum)
#     if sum < dist:
#         dist = sum
#         ret = arr[i][0]


# print(ret)