"""
print 1 to 10
"""
# for i in range(1,11):
#     print(i)
"""
print even numbers btwn 1 and 20
"""
# for i in range(1,21):
#     if i%2==0:
#         print(i)
"""
print odd number btwn 1 and 20
"""
# for i in range(1,21):
#     if i%2!=0:
#         print(i)
"""
print each char of string using for loop
"""
# i="python"
# for ch in i:
#     print(ch)
"""
find sum of number  from 1 to 50
"""
# sum=0
# for i in range(1,51):
#     sum=sum+i
# print(sum)
"""
multiplication of given number
"""
# num=int(input("enter a number:"))
# mul=0
# for i in range(1,num+1):
#     mul=num*i
#     print(i,"*",num,"=",mul)
"""
count num of vowels in given string
"""
# vowels="aeiou"
# count=0
# char=(input("enter a string:"))
# for ch in char:
#     if ch in vowels:
#         count=count+1
# print(count)
"""
reverse the given string
"""
# word="python"

# print(word[5])
# print(word[4])
# print(word[3])
# print(word[2])
# print(word[1])
# print(word[0])
"""
reverse of a given string
"""
# text=input("enter a word:")
# word_length=len(text)-1
# result=""
# for i in range(word_length,-1,-1):
#     result=result+text[i]
# print(result)
    
"""
merge word
"""

word1="abc"
word2="por"
result=""
for i in range(0,3):
    res=word1[i]+word2[i]
    result=result+res
print(result)
