def str_compression():
    str=input("enter your string :")
    count=1
    i=0
    j=1
    while j<len(str):
        if str[i]==str[j]:
            count+=1
            
        else:
            print(str[i],count,sep='',end="")
            i=j 
            count=1
        j+=1
    print(str[i],count,sep='',end='')
str_compression()