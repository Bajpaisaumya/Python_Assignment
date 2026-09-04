def fibb():
    n=int(input("enter the number :"))
    num1=0
    num2=1
    sum=0
    for i in range(n):
        print(num1,end=" ")
        #sum=num1+num2
        num1,num2=num2,num1+num2
        #print(sum)
fibb()