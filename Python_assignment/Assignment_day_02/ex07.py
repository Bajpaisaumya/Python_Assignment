def manual_substring_counter():
    str=input("Enter your text: ")
    target=input("Enter your target string: ")
    count=0;
    for i in range(0,len(str)+1):
        if str[i:i+2]==target:
            count+=1
    print(count)
manual_substring_counter()

        