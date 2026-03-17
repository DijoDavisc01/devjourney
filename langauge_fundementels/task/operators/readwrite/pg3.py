"""
9. Write a program to append new content to an existing file without deleting old data.
"""
file=("four","five","six")
fa=open("langauge_fundementels\\task\\operators\\readwrite\\pg3.txt","a")
for w in file:
    fa.write(w+"\n")

