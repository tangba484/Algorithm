a,b,n = map(int,input().split())

cnt = 0

while 1:
    cnt += 1
    if cnt == n+1:
        print(a//b)
        break
    a = (a % b) * 10