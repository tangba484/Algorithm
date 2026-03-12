n,k = map(int,input().split())

arr = [0,1] + [i for i in range(2,n+1)]

cnt = 0

for idx in range(2,n+1):
    if arr[idx] != 0:
        p = arr[idx]
        i = 1
        while i*p < n+1 :
            if arr[i*p] != 0:
                cnt += 1
            if cnt == k:
                print(arr[i*p])
                break
            arr[i*p] = 0
            i += 1
        
    