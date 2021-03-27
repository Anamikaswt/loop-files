num=int(input("enter the number"))
a=1
sum=0
while num>=a:
    if num%a==0:
        print(a)
    a=a+1
print(sum+a,"is factorial")