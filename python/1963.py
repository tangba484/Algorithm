from collections import deque
n = int(input())

primes = []
for i in range(1000,10000):
    flag = 1
    for j in range( 2, int(i**(1/2) + 1)):
        if i % j== 0:
            flag = 0
            break
    if flag == 1:
        primes.append(i)
for _ in range(n):
    start,end = map(int,input().split())
    visited = [0]*(10000)
    primeMap = [0]*(10000)
    for i in primes:
        primeMap[i] = 1

    q = deque([[start,0]])
    visited[start] = 1
    ans = -1
    while q:
        num,depth = q.popleft()
        if num == end:
            ans = depth
            break
        first_num = num//1000
        second_num = (num // 100)%10
        third_num = num//10%10
        fourth_num = num%10

        for i in range(1,10):
            next_num = i*1000 + second_num*100 + third_num*10 + fourth_num
            if not visited[next_num] and primeMap[next_num] == 1:
                visited[next_num] = 1
                q.append([next_num,depth + 1])
        for i in range(0,10):
            next_num = first_num*1000 + i*100 + third_num*10 + fourth_num
            if not visited[next_num] and primeMap[next_num] == 1:
                visited[next_num] = 1
                q.append([next_num,depth + 1])
        for i in range(0,10):
            next_num = first_num*1000 + second_num*100 + i*10 + fourth_num
            if not visited[next_num] and primeMap[next_num] == 1:
                visited[next_num] = 1
                q.append([next_num,depth + 1])
        for i in range(0,10):
            next_num = first_num*1000 + second_num*100 + third_num*10 + i
            if not visited[next_num] and primeMap[next_num] == 1:
                visited[next_num] = 1
                q.append([next_num,depth + 1])
    if ans == -1:
        print("Impossible")
    else:
        print(ans)