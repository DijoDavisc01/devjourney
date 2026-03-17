signal=input("enter the signal color:")
match signal:
    case "red":print("stop")
    case "green":print("go")
    case "yellow":print("wait")
    case _:print("fool")