N,K = map(int,input().split())

arr = list(map(int,input().split()))


def bub(arr):
    cnt = 0
    for i in range(N):
        for j in range(0,N-1-i):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
                cnt += 1
            if cnt == K:
                return sorted([arr[j],arr[j+1]])
    return [-1]


print(*bub(arr))