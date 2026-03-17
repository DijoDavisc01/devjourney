fr=open("langauge_fundementels\\task\\operators\\readwrite\\flight.txt")
flight=[]
for line in fr:
    data=line.rstrip("\n").split(",")
    di={"year":data[0],"month":data[1],"no_passengers":int(data[2])}
    flight.append(di)
# print(flight)
no_passenger_1949=sum([d.get("no_passengers")for d in flight if d.get("year")=="1949"])
# print("no_of passengers in 1949:",no_passenger_1949)
year_wise_count={}
for p in flight:
    year=p.get("year")
    p_count=p.get("no_passengers")
    if year in year_wise_count:
        year_wise_count[year]+=p_count
    else:
        year_wise_count[year]=p_count
# print(year_wise_count)
# year_wise_count_sort=sorted([[v,k]for k,v in year_wise_count.items()],reverse=True)
year_wise_count_sort=sorted(year_wise_count,key=year_wise_count.get)
print(year_wise_count_sort)