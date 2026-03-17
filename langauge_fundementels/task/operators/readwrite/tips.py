from csv import DictReader
fr=open("langauge_fundementels\\task\\operators\\readwrite\\tips.csv")
data=list(DictReader(fr))
# print(data)
day_wise_tip={}
for t in data:
    day=t.get("day")
    tip=float(t.get("tip"))
    if day in day_wise_tip:
        day_wise_tip[day]+=tip
    else:
        day_wise_tip[day]=tip
# print(day_wise_tip)
day_wise_revenue={}
for r in data:
    day=r.get("day")
    bill=float(r.get("total_bill"))
    if day in day_wise_revenue:
        day_wise_revenue[day]+=bill
    else:
        day_wise_revenue[day]=bill
# print(day_wise_revenue)
sex_wise_tip={}
for t in data:
    sex=t.get("sex")
    tip=float(t.get("tip"))
    if sex in sex_wise_tip:
        sex_wise_tip[sex]+=tip
    else:
        sex_wise_tip[sex]=tip
print(sex_wise_tip)



