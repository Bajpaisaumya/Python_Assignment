def name_anonymizer():
    str=input("enter the name: ")
    str=str.split()
    for i in str:
        if i!=str[-1]:
            print(i[0].upper()+".",end=" ")
        else:
            print(i[0].upper()+i[1:].lower(),end=" ")
name_anonymizer()