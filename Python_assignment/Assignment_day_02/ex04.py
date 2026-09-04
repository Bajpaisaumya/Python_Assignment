def vowel_cononent_count():
    s=input(" enter a string :")
    a=0
    e=0
    i=0
    o=0
    u=0
    consonent=0
    for p in s.lower():
        if p=='a':
            a=a+1
        elif p=='e':
            e=e+1
        elif p=='i':
            i=i+1
        elif p=='o':
            o=o+1
        elif p=='u':
            u=u+1
        elif p.isalpha():
            consonent+=1

    print(" Vowel frequncy :")
    print("a: ", a)
    print("e: ", e)
    print("i :", i)
    print("o :", o)
    print("u :", u)
    print("total consonent: ",consonent)
vowel_cononent_count()

