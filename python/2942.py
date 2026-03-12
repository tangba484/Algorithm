import math
R,G = map(int,input().split())
gcd = math.gcd(R,G)

arr = set([])

for i in range(1, int(gcd**(1/2)) + 1):
    if gcd % i == 0:
        arr.add(i)
        arr.add(int(gcd/i))

for i in arr:
    if gcd % i == 0:
        print(i, int(R/i) , int(G/i))