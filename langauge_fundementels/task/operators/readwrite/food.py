fr=open("langauge_fundementels\\task\\operators\\readwrite\\food.txt")
fd_lst=[lst.rstrip("\n")for lst in fr]
fd_count={lst:fd_lst.count(lst) for lst in fd_lst}
print(fd_count)
fd_count_max=[[v,k]for k,v in fd_count.items()]
print(sorted(fd_count_max,reverse=True))