grade=input("enter grade: ")
match grade:
    case "a":
        print("excellent")
    case "b":
        print("good")
    case "c":
        print("avg")
    case "d":
        print("pass")
    case "e":
        print("fail")
    case _:
        print("invalid")