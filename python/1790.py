n,k = map(int,input().split())

a = len(str(n))
maxL = 0
for i in range(1,a+1):
    if i == a:
        maxL += (n - 10**(i-1) + 1) * a
    else:
        maxL += 9 * (10**(i-1)) * i

if maxL < k:
    print(-1)
else:
    c = 1
    while 1:
        k -= 9*(10**(c-1))*c
        if k <= 0:
            k += 9*(10**(c-1))*c
            break
        c += 1
    if k%c == 0:
        print(str(10**(c-1) + k//c -1)[-1])
    else:
        print(str(10**(c-1) + k//c)[k%c-1])