from collections import deque
n,k = map(int,input().split())

arr = deque([i for i in range(1,n+1)])

ans = []

while arr:
    arr.rotate(-k + 1)
    ans.append(arr.popleft())
print("<"+str(ans)[1:-1]+">")