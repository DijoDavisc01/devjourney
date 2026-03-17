fr=open("langauge_fundementels\\task\\operators\\readwrite\\food_logs.txt")
food_logs=[]
for line in fr:
    data=line.rstrip("\n").split(",")#line 1="1,break_fast,idly,175,11-1-2025,hari"
    log={"id":data[0],"meal_type":data[1],"name":data[2],"calories":float(data[3]),"date":data[4],"owner":data[5]}
    food_logs.append(log)
print(food_logs)

