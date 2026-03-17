# num=int(input("enter a number:"))
# sum=0
# for i in range(1,num):
#     if num%i==0:
#         sum=sum+i
# if num==sum:
#     print(num,"perfect number")
# else:
#     print(num,"not perfect number")
"""
 palindrome
"""
# word=input("enter a word:")
# word_len=len(word)-1
# result=""
# for i in range(word_len,-1,-1):
#     result=result+word[i]
# if result==word:
#     print(word,"is plaindrome")
# else:
#     print(word,"is not palindrome")
"""
removing balance of 2 words
"""
# text="python programming"
# print(text[7:14])
# print(text[:6])
# print(text[7:])
# text1=input("enter a word1:")
# text2=input("enter a word2:")
"""
slice a word to first and last
"""
# word="dijodavis3@gmail.com"
# first=(word[:10])
# last=(word[10:])
# print(first)
# print(last)

text1=input("enter a word1:")
text2=input("enter a word2:")
if len(text1)>len(text2):
    print(text1[len(text2):])
elif len(text2)>len(text1):
    print(text2[len(text1):])
else:
    print("no difference")