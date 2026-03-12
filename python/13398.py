n = int(input())
arr = list(map(int,input().split()))


dpa=[0]*(n)
dpb=[0]*(n)
dpa[0] = arr[0]
dpb[0] = arr[0]
ans = arr[0]
for i in range(1,n):

    dpa[i] = max(dpa[i-1]+arr[i],arr[i])

    dpb[i] = max(dpb[i-1] + arr[i],dpa[i-1])

    ans = max(ans,dpa[i],dpb[i])
print(ans)