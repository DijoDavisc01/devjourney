"""

"""
# watch={"brand":"boat","color":"black","type":"smart","model":"wavelite","strap":"silcon"}
# # print(watch)
# watch["strap"]="chain"
# print(watch)
"""
create a dict of product which contain id,title,price,avl_qty
"""
# product={"id":12,"title":"thar","price":2000000,"avl_qty":28500}
# # print(product["title"])
# # product["avl_qty"]+=10
# # print(product["avl_qty"])
# # product["code"]="sku12"#adding a new key and value
# # print(product)
# if "offer" in product:# check a key in dictionay
#     print("yes")
# else:
#     print("no")
"""
Create a dictionary to store a student's details:
id
name
course
marks
Tasks:
Print the student name
Update marks by adding 5 bonus marks
Add a new key grade
Check if attendance key exists
"""
# student={"id":1,"name":"dijo","course":"bca","marks":59}
# print(student["name"])
# student["marks"]+=5
# print(student)
# student["grade"]="A"
# print(student)
# if "attendence" in student:print("attendance key exists:yes")
# else: print("attendance key exists:no")
"""
Create a dictionary:
account_number
holder_name
balance
Tasks:
Deposit 5000
Withdraw 2000
Check if balance is less than 1000 → print "Low Balance"
"""
# sbi={"acc_no":2311000008832,"holder_nmae":"dijo","bal":621}
# sbi["bal"]+=5000
# print(sbi)
# if sbi["bal"]>=2000:
#     sbi["bal"]-=2000
#     print("you got your noney, bal=",sbi["bal"])
# else:print("insufficient bal..")
# if sbi["bal"]<=1000:print("low balance")
# else:print("bal is greater than 1000 ...superrrrr...")
"""
daily calories
"""
#calories={"sun":2100,"mon":1800,"tue":1800,"wed":1980,"thur":1600,"fri":1820,"sat":1900}
# total_calories=0
# calories=
# for key in calories:
#     #print(key,calories[key])
#     total_calories+=calories[key]
# print(total_calories)
# print(total_calories/len(calories))
"""
sales report
"""
# sales={"sun":21000,"mon":21800,"tue":21800,"wed":21980,"thur":21600,"fri":21820,"sat":21900}
# total_sale=0
# found = False
# for key in sales:
#     print(key,sales[key])
#     total_sale+=sales[key]
# print("total_sale:",total_sale)
# avg=total_sale/len(sales)
# print("avg sale:",avg)  
# for key in sales:
#     if sales[key]<avg:
#         print(key)
#         found = True
#         break
       
# if found == False:

#     print("Poda")
"""
class dict
"""
employee={"id":101,"name":"dijo","sal":100000,"dept":"qa"}
# print(employee.keys())
# employee.values()
# print(employee.values())
# for key in employee.keys():
#     print(key)
# for val in employee.values():
#     print(val)
# for k,v in employee.items():
#     print(k,v)
# print(employee.get("name"))#dijo
# print(employee.get("tag"," tag idhil illa mone"))#tag idhil illa mone enn return cheyum 
# print(employee.get("tag"))#none return cheyum key illange
# employee.pop("name")""" to remove a value by calling key"""
# print(employee)
# """ to update with new key and value"""
# employee["bonus"]=25000
# print(employee)
# """ to add value"""
# employee["sal"]+=25000 
# print(employee)
manali={"dijo":300,"akash":1000,"edwin":800,"alan":15000,"subin":0,"manoj":0}
total_exp=0
for v in manali.values():
    total_exp+=v
print(total_exp)
eql_split=round(total_exp/len(manali))
print(eql_split)
spend_wise={}
for k,v in manali.items():
    payment=eql_split-v
    spend_wise[k]=payment
print(spend_wise)
