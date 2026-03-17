num1=int(input("enter a number: "))
num2=int(input("enter a number: "))
operator=input("enter operator")
match operator:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)
    case "%":
        print(num1%num2)
    case _:
        print("run this way----->")

