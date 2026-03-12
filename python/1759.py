L,C = map(int,input().split())

arr = sorted(list(input().split()))

aeiou = ["a","e","i","o","u"]
visited = [0]*(C)
def back(lst,start):
    leng = len(lst)
    if leng == L:
        aeiou_cnt = 0
        for i in aeiou:
            if i in lst:
                aeiou_cnt += 1
        if aeiou_cnt >= 1 and leng - aeiou_cnt >= 2:
            print(*lst,sep="")
            return True
        else:
            return False
    
    for i in range(start,C):
        if not visited[i]:
            visited[i] = 1
            back(lst + [arr[i]],i + 1)
            visited[i] = 0

back([],0)