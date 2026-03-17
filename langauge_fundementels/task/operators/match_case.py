number=int(input(" enter a number:"))
match number:
    case 0:print("zero")
    case _ if number<0:print("-ve")
    case _ if number>0:print("+ve")
    case _:print("heyy bayyaaaa....")

