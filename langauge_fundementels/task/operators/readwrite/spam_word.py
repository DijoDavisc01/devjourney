def spam_count(message):

    fr=open("langauge_fundementels\\task\\operators\\readwrite\\spam_words.txt")
    spam_lst=[line.rstrip("\n") for line in fr]
    spam_word=[w for w in message.split(" ") if w in spam_lst]
    count=len(spam_word)
    return count
print(spam_count("bonus cash"))

"""
"""
# def spam_word_count(message):

#     count = 0

#     fr = open("13. ErrorHandling\\spam_words.txt")

#     spam_words = [line.strip() for line in fr]

#     for w in message.split(" "):

#         if w in spam_words:

#             count += 1

#     return count

# print(spam_word_count("bonus cash edwin debt"))

