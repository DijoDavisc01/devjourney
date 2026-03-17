"""
* 
* * 
* * * 
* * * * 
* * * * * 
"""
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
"""
1
2 3
4 5 6
7 8 9 10
"""
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
"""
* * * * *
*       *
*       *
*       *
* * * * *      
"""
# for i in range(1,6):
#     for j in range (1,6):
#         if i==1 or i==5 or j==1 or j==5:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
"""
* * * * * 
* * * * 
* * *
* *
*

"""
# for i in range(1,6):
#     for j in range(6,i,-1):
#         print("*",end=" ")
#     print()
"""
* * * * 
  * * * * 
    * * * * 
      * * * * 
        * * * * 
"""
# for i in range(1,6):
#     for s in range(1,i):
#         print(" ",end=" ")
#     for j in range(4,0,-1):
#         print("*",end=" ")
#     print()
"""
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
"""
# for i in range(5,0,-1):
#     for s in range(1,i):
#         print(" ",end=" ")
#     for j in range(1,5-i+2):
#         print("*",end=" ")
#     print()
"""
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
"""
# for i in range(1,6):
#     for s in range(1,i):
#         print(" ",end=" ")
#     for j in range(6,i,-1):
#         print("*",end=" ")
#     print()
"""
*   *   *   *   *  
   *   *   *   *  
     *   *   *  
       *   *  
         *  
"""
# for i in range(1,6):
#     for s in range(1,i):
#         print(" ",end=" ")
#     for j in range(6,i,-1):
#         print(" * ",end=" ")
#     print()
"""
           *  
         *   *  
       *   *   *  
     *   *   *   *  
   *   *   *   *   *  
 *   *   *   *   *   *  
"""
# for i in range(6,0,-1):
#     for s in range(1,i):
#         print(" ",end=" ")
#     for j in range(1,6-i+2):
#         print(" * ",end=" ")
#     print()
"""
"""
for i in range(6,0,-1):
    for s in range(1,i):
        print(" ",end=" ")
    for j in range(1,6-i+2):
        print(" * ",end=" ")
    print()
for i in range(1,7):
    for s in range(1,i):
        print(" ",end=" ")
    for j in range(7,i,-1):
        print(" * ",end=" ")
    print()