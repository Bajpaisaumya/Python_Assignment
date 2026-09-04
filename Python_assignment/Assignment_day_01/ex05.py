def calc():
    n1=int(input("enter the first number "))
    n2=int(input(" enter the second number "))
    operator=input("enter the operator(+,-,/,*,%) :")
    match operator:
        case "+":
            print(n1+n2)
        case "-":
            print(n1-n2)
        case " /":
            print(n1/n2)
        case "*":
            print(n1*n2)
        case "%":
            print(n1%n2)
        case _:
            print('invalid input')
        
calc()

    