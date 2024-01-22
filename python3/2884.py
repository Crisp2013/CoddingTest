(hour,min)=list(map(int, input().split()))

min=min-45
if min<0:
    min=min+60
    hour=hour-1
if hour<0:
    hour=23
print(str(hour)+" "+str(min))