def f(n):
    ans = ""
    while n :
        ans += str(n%2)
        n = n // 2
    if ans == "":
        ans = "0"
    return ans[::-1]
import sys
input = sys.stdin.readline

k = int(input())
for _ in range(k):

    a,b = (input().split())
    a,b = int(a,2) , int(b,2)
    print(f(a+b))




