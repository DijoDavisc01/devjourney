"""
revserse of string
"""
# text="dijo davis"
# word=text[::3]
# print(word)
# reversed=text[::-1]
# print(reversed)
"""
print row and col
"""
# for r in range(1,5):
#     for c in range(1,7):
#         print(f"row{r}column{c}")
#     print(f"exicution completed row:{r}")
"""
\n,\t etc...
"""
# print("hello",end="\t")
# print("world")
# for r in range(1,5):
#     for c in range(1,7):
#         print(r,c,end="\t")
#     print()
"""
1 2 3 4
1 2 3 4
1 2 3 4
"""
# for r in range(1,4):
#     for c in range(1,5):
#         print(c,end="\t")
#     print()
"""
o e o e
o e o e
o e o e
o e o e
"""
# for r in range(1,5):
#     for c in range(1,5):
#         if c==1 or c==3:
#             print("o",end="\t")
#         else:
#             print("e",end="\t")
#     print()
"""
1 0 0
0 1 0
0 0 1
"""
# for r in range(1,4):
#     for c in range(1,4):
#         if r==c:
#             print("1",end="\t")
#         else:
#             print("0",end="\t")
#     print()
"""
1 1 1 1
1 0 0 1
1 0 0 1
1 1 1 1 
"""
for r in range(1,5):
    for c in range(1,5):
        if r==1 or r==4 or c==1 or c==4:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()

"""
1 1 1 1 
0 0 0 0
1 1 1 1 
0 0 0 0 
"""
# for r in range(1,5):
#     for c in range(1,5):
#         if r==1 or r==3:
#             print(1,end="\t")
#         else:
#             print(0,end="\t")
#     print()