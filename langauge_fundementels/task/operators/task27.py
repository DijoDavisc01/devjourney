"""
Task 26 || Dataset || 03-03-2026 


Observe the dataset and create your own set of questions based on it.
1.total of bill
2.display minimum tip
3.display count male & female smokers
4.total max tip in sundays
5.find lunch or dinner is more 
6.count of size and unique size
"""
tips_data = [
    {"total_bill": 16.99, "tip": 1.01, "sex": "Female", "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 2},
    {"total_bill": 10.34, "tip": 1.66, "sex": "Male",   "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 3},
    {"total_bill": 21.01, "tip": 3.50, "sex": "Male",   "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 3},
    {"total_bill": 23.68, "tip": 3.31, "sex": "Male",   "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 2},
    {"total_bill": 24.59, "tip": 3.61, "sex": "Female", "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 4},
    {"total_bill": 25.29, "tip": 4.71, "sex": "Male",   "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 4},
    {"total_bill": 8.77,  "tip": 2.00, "sex": "Male",   "smoker": "Yes", "day": "Sun",  "time": "Dinner", "size": 2},
    {"total_bill": 26.88, "tip": 3.12, "sex": "Male",   "smoker": "Yes", "day": "Sun",  "time": "Dinner", "size": 4},
    {"total_bill": 15.04, "tip": 1.96, "sex": "Male",   "smoker": "Yes", "day": "Sun",  "time": "Dinner", "size": 2},
    {"total_bill": 14.78, "tip": 3.23, "sex": "Female", "smoker": "Yes", "day": "Sun",  "time": "Dinner", "size": 2},
    {"total_bill": 10.27, "tip": 1.71, "sex": "Male",   "smoker": "No",  "day": "Sat",  "time": "Dinner", "size": 2},
    {"total_bill": 35.26, "tip": 5.00, "sex": "Female", "smoker": "Yes", "day": "Sat",  "time": "Dinner", "size": 4},
    {"total_bill": 15.42, "tip": 1.57, "sex": "Male",   "smoker": "No",  "day": "Sat",  "time": "Dinner", "size": 2},
    {"total_bill": 18.43, "tip": 3.00, "sex": "Male",   "smoker": "No",  "day": "Sat",  "time": "Dinner", "size": 4},
    {"total_bill": 14.83, "tip": 3.02, "sex": "Female", "smoker": "No",  "day": "Sat",  "time": "Dinner", "size": 2},
    {"total_bill": 21.58, "tip": 3.92, "sex": "Male",   "smoker": "Yes", "day": "Fri",  "time": "Dinner", "size": 2},
    {"total_bill": 10.33, "tip": 1.67, "sex": "Female", "smoker": "No",  "day": "Fri",  "time": "Lunch",  "size": 2},
    {"total_bill": 16.29, "tip": 3.71, "sex": "Male",   "smoker": "Yes", "day": "Fri",  "time": "Lunch",  "size": 3},
    {"total_bill": 13.37, "tip": 2.00, "sex": "Female", "smoker": "No",  "day": "Thur", "time": "Lunch",  "size": 2},
    {"total_bill": 12.69, "tip": 2.31, "sex": "Male",   "smoker": "Yes", "day": "Thur", "time": "Lunch",  "size": 2},
    {"total_bill": 17.92, "tip": 4.08, "sex": "Male",   "smoker": "No",  "day": "Thur", "time": "Lunch",  "size": 2},
    {"total_bill": 20.29, "tip": 2.75, "sex": "Female", "smoker": "Yes", "day": "Thur", "time": "Lunch",  "size": 2},
    {"total_bill": 15.77, "tip": 2.23, "sex": "Male",   "smoker": "No",  "day": "Thur", "time": "Lunch",  "size": 2},
    {"total_bill": 39.42, "tip": 7.58, "sex": "Male",   "smoker": "Yes", "day": "Sat",  "time": "Dinner", "size": 4},
    {"total_bill": 19.82, "tip": 3.18, "sex": "Female", "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 2}
]
total_bill=sum([l.get("total_bill") for l in tips_data ])
# print(total_bill)
min_tip=min(l.get("tip") for l in tips_data)
# print(min_tip)
female_smokers=[l for l in tips_data if  l.get("sex")=="Female" and l.get("smoker")=="Yes"]
male_smokers=[l for l in tips_data  if l.get("sex")=="Male" and l.get("smoker")=="Yes"]
male_female_smokers={"females_smoker":len(female_smokers),"male_smokers":len(male_smokers)}
# print(male_female_smokers)
max_sunday_tip=max([l.get("tip")for l in tips_data if l.get("day")=="Sun"])
# print(max_sunday_tip)
lunch_time=len([l for l in tips_data if l.get("time")=="Lunch"])
dinner_time=len([l for l in tips_data if l.get("time")=="Dinner"])
unique_size={l.get("size")for l in tips_data}
# print(unique_size)