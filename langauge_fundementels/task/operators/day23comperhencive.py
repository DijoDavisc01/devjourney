
"""
slicing
"""
# lst=[10,20,30,40,50,60]
# portion=lst[0:4]
# print(portion)
# portion2=lst[2:]
# print(portion2)
# portion3=lst[:5]
# print(portion3)
# lst_copy=lst[::]
# print(lst_copy)
"""
comprehence is easy way for creating a sequence from a sequence ..when it is list[left middle  right][return iteration condition]
"""
# arr=[1,2,3,4,5,6]
# sqr=[n**2 for n in arr]
# print(sqr)
# qube={n**3 for n in arr}
# print(qube)
"""
print a list of 10 num
"""
# lst=[i for i in range(1,11)]
# print(lst)
"""
create a list of double of each element
"""
# lst=[2,4,6,8,10]
# d_lst=[n*2 for n in lst]
# print(d_lst)
"""
create a list of even num from range of 20 to 50
"""
# lst=[i for i in range(20,51) if i%2==0]
# print(lst)
"""
create a new list that contain words len>3
"""
# words=["apple","cat","orange","me","array"]
# n_words=[n for n in words if len(n)>3]
# print(n_words)
"""
create a list that contain recursive num
"""
# lst=[10,11,10,11,12,13,14,15,16,15]

# n_lst={n for n in lst  if lst.count(n)>1}
# print(n_lst)
"""
create a list the words contail palindrome
"""
# lst=["mad","test","tan","racecar","dad"]
# p_lst=[w for w in lst if w[::-1]==w]
# print(p_lst)
"""
creat a dict using the list key should be values of list and values should be the count
"""
# lst=[10,11,10,12,13,14,15,14,16,16,16]
# dic={n:lst.count(n) for n in lst}
# print(dic)
"""
char count
"""
# word="racecar"
# word_c={w:word.count(w) for w in word}
# print(word_c)
"""
print non recursive char and print cahr count>2
"""
# word="racecarfast"
# r_char=[c for c in word if word.count(c)==1]
# print(r_char)
# c_char={c:word.count(c) for c in word if word.count(c)>2}
# print(c_char)
"""
word count
"""
# text="python programing programing langauge is simple"
# word=text.split(" ")
# word_count={w:word.count(w) for w in word}
# print(word_count)
"""
"""
# orders=["tea","coffe","idly","coffe","tea","dosa","tea","coffe"]
# word_c={w:orders.count(w) for w in orders}
# print(word_c)
"""

"""