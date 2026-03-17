
# print(dir(str))
# print(dir(list))
# print(dir(int))
# food_logs=["rice and elisery","water","rise and eliseri","water"]
# food_logs[2]="biriyani and chikencurry"# update in list by changing item
# # print(food_logs)
# # print(food_logs[3])
# # for i in range(0,4):
# #     print(food_logs[i])
# for f in food_logs:
#     print(f)
"""
attendence of week
"""
# attend=['p','p','p','p','p','h','h','p']
# count_p=0
# count_h=0
# for att in attend:
#     if att=='p':
#         count_p+=1
#     elif att=='h':
#         count_h+=1
# print(count_h,count_p)
"""
expence of year
"""
# exp=[1200,1210,1220,1230,1240,1100,1300,1300,1360,1400,1280,1450]
# total=0
# avg=0
# length=len(exp)
# for ex in exp:
#     total=total+ex
# print(total)
# print(total/length)
"""
append used to add object in the end of list
"""
colors=["red","red","green","blue"]
# colors.append("black")
# print(colors)
"""
insert is used to add an object in list using index
"""
# colors.insert(2,"yellow")
# print(colors)
"""
pop is used to remove a item using index(default value is -1 so remove last object in list)
"""
# colors.pop(2)
# print(colors)
"""
remove is used to remove an object by calling its name
"""
# colors.remove("blue")
# print(colors)
"""
count is used to find no of count of an object in list
"""
# print(colors.count("red"))
"""
copy is used to copy the list to another address
"""
#mycolors=colors.copy()
# print(mycolors)
"""is    is an identity operator to check variable is stored in same memory or not"""
# print(colors is mycolors)
""" 
== is used to compare the values
"""
# print(mycolors==colors)
""" sort is used to change acending or decending order"""
# colors.sort()
# print(colors)
# num=[1,2,3,4,8,7,6,5]
# num.sort()
# print(num)
# num.sort(reverse=True)
# print(num)
"""
extend used to add new list objects to previous one
"""
# new_colors=["white","black"]
# colors.extend(new_colors)
# print(colors)
"""
w.a.p to create 2 list pos and neg list from given list
"""
# num=[-1,-2,-3,1,2,3]
# pos=[]
# neg=[]
# for n in num:
#     if n>0:
#         pos.append(n)
#     else:
#         neg.append(n)
# print(pos)
# print(neg)
"""
two list for sqr and qube frome given
"""
# num=[1,2,3]
# sqr=[]
# cube=[]
# for n in num:
#     sqr.append(n**2)
#     cube.append(n**3)
# print(sqr)
# print(cube)
"""

"""
# stk1=[10,11,12,13]
# stk2=[20,21,22,23]
# stk1.extend(stk2)
# update_stk=[]
# for s in stk1:
#     update_stk.append(s+5)
# print(update_stk)
    
"""
map is used to apply functionality value
filter is used when there is a condition
reduce ,to specific value
"""