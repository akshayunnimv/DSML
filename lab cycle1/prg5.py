for i in range(1,1001):
    number=str(i)
    numlen=len(number)
    sum=0
    temp=i
    while(i>0):
        sum=sum+((i%10)**numlen)
        i=i//10
    if(sum==temp):
        print(temp)

