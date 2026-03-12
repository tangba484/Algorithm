from collections import deque
n,k = map(int,input().split())

arr = deque([i for i in range(1,n+1)])


while len(arr)>=k:
    a = arr.popleft()
    arr.append(a)
    for i in range(k-1):
        arr.popleft()
print(arr[0])