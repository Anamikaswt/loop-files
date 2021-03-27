question_list = [
    "How many continents are there?",              # pehla question
    "What is the capital of India?",            # doosra question
    "NG mei kaun se course padhaya jaata hai?"    # teesra question
]
options_list = [
    #pehle question ke liye options
    ["Four", "Nine", "Seven", "Eight"],
    #second question ke liye options
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    #third question ke liye options
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
# har ek question ke liye, uski solution key (yeh index nahi hai)
solution_list = [3, 4, 1]
answer=["seven","delhi","software engineering"] 
print("welcome to KBC") 
i=0
while i<len(question_list):
    m=question_list[i]
    print(m)
    j=0
    k=i
    while j< len(options_list[i]):
        n=options_list[k][j]
        print(j+1,n)
        j=j+1
    b=input("do you want to use 5050 lifeline")
    if b=="yes":
        print(1,options_list[i][i])
        print(2,answer[i])
    ans=int(input("enter the number"))
    if solution_list[i]==ans or 2==ans:
        print("your answer is correct")
    else:
        print("your answer is wrong")
        break
    i=i+1
    print("congratulation ! you won KBC ")