def wizards_magic_bag():
    list=(input("Insert the values in list :")).split()
    list1=[]

    list1=list
    
    str=input("Enter a new word:")
    print("Portal transition activated!")

    if str!='':
        list1.append(str)
        str_remove=list1.pop(0)
        print(f"Ejected oldest item: staff:{str_remove}")
    print(f"Current items in the magic bag: {list}")
    
wizards_magic_bag()


