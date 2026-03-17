def skill_extract(skills):
    res=""
    fr=open("langauge_fundementels\\task\\operators\\readwrite\\skill.txt")
    skill_lst=[l.rstrip("\n").lower() for l in fr]
    word_lst=[w for w in skills.split(" ") if w in skill_lst]
    res=" ".join(word_lst)
    return res
print(skill_extract("skills in python css html java javascript etc .."))