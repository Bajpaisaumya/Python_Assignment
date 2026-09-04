def format():
    str=input("enter your string: ")
    for i in str.split():
        print(i[0].upper() + i[1:].lower(),end=' ')
format()