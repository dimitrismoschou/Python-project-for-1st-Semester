a=input("dwse ena diastima")
n=1
k=1
temp=5
while (temp==5):
    if (a[n:n+1]==",") :
        if (k!=1):
            b=a[n+1-k:n]
            temp=6
    else:
        n=n+1
        k=k+1   #vriskei ton arithmo a se ena diastima [a,b]
k=1
while (temp==6):
    if (a[n+1:n+2]=="]"):
        if (k!=1):
            c=a[n+2-k:n+1]
            temp=7
    else:
        n=n+1
        k=k+1   #vriskei ton arithmo b se ena diastima [a,b]
d=input("dwse enan akeraio")
sum=0
for i in range(int(b),int(c)+1):
    sum1=0
    for j in range(int(b),int(c)+1):
            if int(i%j)==0:
                    sum1=sum1+1
    if (sum1==2):
             sum=sum+1  #vriskei tous prwtous arithmous se ena diastima [a,b]
sum=sum+1
list1=[0]*sum

sum=0
l=1
for i in range(int(b),int(c)+1):
    sum1=0
    for j in range(int(b),int(c)+1):
            if int(i%j)==0:
                    sum1=sum1+1
    if (sum1==2):
             sum=sum+1
             list1[l]=i
             l=l+1  #emfanizei olous tous prwtous arithmmous se ena diastima [a,b]
sum2=0
for i in range (1,sum):
    for j in range(1,sum):
         if int(d)==abs(list1[i]-list1[j]):
            sum2=sum2+1
sum2=sum2*2+1
list2=[0]*sum2
x=1
for i in range (1,sum):
    for j in range(1,sum):
         if int(d)==abs(list1[i]-list1[j]):
            list2[x]=list1[i]
            list2[x+1]=list1[j]
            x=x+2
         
print("to zevgos twn dyo prwtwn einai to " ,list2[1],"kai to",list2[2])

             

    

         

