t=(int)(input()) #No of values 
Arr=[]
Arr=list(map(int,input().split(' ')[:t]))
d=max(Arr)
print(Arr.count(d))
