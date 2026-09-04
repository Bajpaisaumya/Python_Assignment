def mail_extract():
    s=input("write your mail:")
    for i in s:
        if i=='@':
            continue;
        print(i,end="")
mail_extract()
