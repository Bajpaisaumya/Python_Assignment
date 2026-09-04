def prime_num():
    n=int(input("enter the number :"))
    if n<2:
        print(" not a prime number")
    digit=n//2
    for i in range(2,digit+1):
        if n%2==0:
            print("it is not a prime number")
            return
        
    print(" it is a prime number")
prime_num()