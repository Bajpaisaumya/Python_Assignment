def cipher_encrypted():
    str=input("enter the text:")
    shift=int(input("enter the value of shift :"))
    res=''
    for i in str:
        if i.isupper():
            res=chr(((ord(i)-ord("A"))+shift)% 26 +ord("A"))
            print(res,end="")
        else:
            res=chr(((ord(i)-ord("a"))+shift)% 26 +ord("a"))
            print(res,end="")
cipher_encrypted()
