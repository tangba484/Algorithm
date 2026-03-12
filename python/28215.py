from itertools import combinations
import math
n,k = map(int,input().split())
arr =[]
ans = []

for _ in range(n):
    arr.append(list(map(int,input().split())))

for i in (combinations([i for i in range(n)],k)):
    Ma = 0
    for j in range(n):
        lst = []
        if j not in (i):
            Mi = float("inf")
            for m in (i):
                X1 = arr[m][0]
                Y1 = arr[m][1]
                X3 = arr[j][0]
                Y3 = arr[j][1]
                d1 = abs(X3-X1) + abs(Y3 - Y1)
                Mi = min(d1,Mi)
            Ma = max(Mi,Ma)
    ans.append(Ma)
print(min(ans))