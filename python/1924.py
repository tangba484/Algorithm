x,y = map(int,input().split())

m = dict({0:0, 1:31 , 2:28,3:31,5:31,7:31,8:31,10:31,12:31,4:30,6:30,9:30,11:30})
day = ["MON", "TUE","WED", "THU", "FRI", "SAT","SUN"]
cnt = 0

for i in range(1,x+1):
    cnt += m[i-1]
cnt = cnt + y - 1

print(day[cnt%7])