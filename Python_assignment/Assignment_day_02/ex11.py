def word_anagrams():
    words=input("enter the words:").split()
    list=[]
    for word in words:
        found=False
        for grp in list:
            if sorted(word)==sorted(grp[0]):
               grp.append(word)
               found=True
               break
        if found==False:
            list.append([word])
               
    print(list)
word_anagrams()


