fr=open("langauge_fundementels\\task\\operators\\readwrite\\all_std.txt","r")
fr1=open("langauge_fundementels\\task\\operators\\readwrite\\passedstd.txt","r")
fw=open("langauge_fundementels\\task\\operators\\readwrite\\failedst.txt","w")
all_std_lst=[l.strip("\n")for l in fr]
passed_std=[l.strip("\n")for l in fr1]
fail_std=set(all_std_lst).difference(passed_std)
print(fail_std)
for l in fail_std:
    fw.write(l+"\n")
