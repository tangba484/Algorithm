n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort()
dp = [1]*(n+1)


for i in range(1,n):
    for j in range(i):
        if arr[j][1] > arr[i][1]:
            