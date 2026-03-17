"""
6. Write a Python program to create a file and write 5 lines of text into it.
"""
file=["manga","munthri","mathnga","peechinga"]
fw=open("langauge_fundementels\\task\\operators\\readwrite\\file.txt","w")
for f in file:
    fw.write(f+"\n")