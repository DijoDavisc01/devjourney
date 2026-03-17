system=input("enter prompt: ")
match system:
    case "start":print("system is starting...")
    case "stop":print("system is stoping..")
    case "restart":print("system is restarting..")
    case _:print("run away ---->")