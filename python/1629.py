a,b,c = map(int,input().split())



def f(a,b):
    if b == 2:
        return (a ** 2) %c
    elif b == 1:
        return a %c
    

    if b%2 == 0:
        res = f(a,b//2)
        return  (res%c * res%c)%c
    elif b%2 == 1:
        res = f(a,b//2)
        return (res%c * res%c * a)%c
print(f(a,b))