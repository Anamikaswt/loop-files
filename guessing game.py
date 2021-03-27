i=5
num=1
num1=10
while num<=num1:
    j=int(input("enter the number"))
    if j==i:
        print("guessing game is correct")
    elif j!=i and j<num1:
        print("not correct","yes you have",num1-num,"chance" )
    else:
        print("no more chance")
    num1=num1-j