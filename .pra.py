def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
a,b=  map(int,input().split())
print(int((a*b)/gcd(a,b)))