n = int(input())
arr = [input() for _ in range(n)]
for i in range(n):
    s = arr[i]
    cnt = 0
    for j in s:
        if j.isdigit():
            cnt += int(j)
    arr[i] = [s,cnt]
arr.sort(key = lambda x : (len(x[0]),x[1],x[0]) )

for i in arr:
    print(i[0])