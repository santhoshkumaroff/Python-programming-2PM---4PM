# n=5 
# val=1
# for i in range(1,n+1): #1
#     for j in range(n): #0 #1 #2 #4 #5
#         print(val,end=" ") # 1
#         val+=1
#     val=1
#     print()

    
    
# # o/p 
# '''
# 1 1 1 1 1 1
# 2 
# '''
# n=5
# val=0
# for i in range(n):
#     for j in range(n):
#         print(chr(65+val),end=" ")
#     val+=1
#     print()
    
# n =5
# * * * * *
# for i in range(n):
#     print("*",end="-") #* * * * *

# print(1,end=" ") #1
# print(1) #2
# print(1) #3
# print(1) #4
# print(1) #5
# print(1) #6

# 5
# n=5
# 1 2 3 4 5 
# for i in range(1,n+1):
#     print(i,end=" ")

# val=1
# for i in range(n): #0 1 2 3 4
#     print(val,end=" ")
#     val+=1
    
# n = 5 
# 5 4 3 2 1

# for i in range(n,0,-1): # 5,0 - 5,4,3,2,1 # 5+1=>6
#     print(i,end=" ") # i =5 
    
# n=6
# A B C D E F
# ord -> number or we can ascii
# chr -> 
# for i in range(n):#0 1 2 3 4 5
#     print(chr(65+i),end=" ") # chr(65+0) => chr(65)=> A # chr(65+1)=> chr(66) =>B # chr(65+2) => C => chr(65+3)=> D => chr(65+4)=>E
    
# v=0
# for i in range(n):
#     print(chr(65+v),end=" ")
#     v+=1

# n =5 # 5-1 => 4
# # E D C B A
# # for i in range(n,-1,-1): #4 3 2 1 0
# #     print(chr(65+i),end=" ")
    
# val = n-1 # 4 3
# for i in range(n): # 0 1 2 3 4
#     print(chr(65+val),end=" ") # 65+4 =>69 => E D
#     val-=1

# n = 5
# A * C * E
# 0 1 2 3 4
# n=5
# for i in range(n): # 0 1 2 3 4 o/p=> A * C * E
#     if i%2==0: # 0
#         print(chr(65+i),end=" ")
#     else:
#         print("*",end=" ")
        
# n = 5
# A * B * C

# n=5
# v=0
# for i in range(n):
#     if i%2==0:
#         print(chr(65+v),end=" ")
#         v+=1
#     else:
#         print("*",end=" ")

# n = 30 # 5 A B C D E
# # A B C D E.........ZABCD or some special character
# val=0
# for i in range(n):
#     if val == 26:
#         val=0
#     print(chr(65+val),end=" ")
#     val+=1

# square pattern
''' col 1 2 3 4 5
row = 1 * * * * *
row = 2 * * * * *
row = 3 * * * * *
row = 4 * * * * *
row = 5 * * * * *
'''
# n=5
# for i in range(1,n+1): # 1 2 3 4 5
#     for j in range(1,n+1): #1 2 3 4 5
#         print("*",end=" ") # * * * * *
#     print()
    
'''
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
'''
n=5
# method 1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end=" ")
#     print()
# method 2
val=1 #2
# for i in range(1,n+1): # for i in range(n)
#     for j in range(1,n+1):# 1 2 3 4 5
#         print(val,end=" ")
#     val+=1
#     print()
    
'''
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''
# n=5
# for i in range(1,n+1):
#     val=1
#     for j in range(1,n+1):
#         print(val,end=" ")
#         val+=1
#     print()

'''
A A A A A
B B B B B
C C C C C
D D D D D
E E E E E
'''
# method 1 
# n=5
# for i in range(n): # 0 1 2 3 4
#     for j in range(n): # 0 1 2 3 4
#         print(chr(65+i),end=" ") # 65+1 # 65+1 # 65+1 #65+1 #65+1
#     print()

# method 2 
# n=5 
# v=0
# for i in range(n):
#     for j in range(n):
#         print(chr(65+v),end=" ")
#     v+=1
#     print()

'''
A B C D E
A B C D E
A B C D E
A B C D E
A B C D E
'''
n=5 
# for i in range(n):
#     v=0
#     for j in range(n):
#         print(chr(65+v),end=" ")
#         v+=1
#     print()

# n=5 
# for i in range(n):
#     for j in range(n):
#         print(chr(65+j),end=" ")
#     print()
'''
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
'''
# method 1 
# n=5
# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         print(j,end=" ")
#     print()
# method 2
# n =5
# for i in range(n):
#     v=n
#     for j in range(n):
#         print(v,end=" ")
#         v-=1
#     print()
'''
n=5
E D C B A
E D C B A
E D C B A
E D C B A
E D C B A
'''
# n=5-1
# for i in range(n,-1,-1):
#     for j in range(n,-1,-1):
#         print(chr(65+j),end=" ")
#     print()
# n=5-1 
# for i in range(n+1):
#     v=n
#     for j in range(n+1):
#         print(chr(65+v),end=" ")
#         v-=1
#     print()  
'''
1 2 3 4 5
* * * * *
1 2 3 4 5
* * * * *
1 2 3 4 5
'''
# n=5
# for i in range(n):
#     for j in range(1,n+1):
#         if i%2==0:
#             print(j,end=" ")
#         else:
#             print("*",end=" ")
#     print()
# n = 5
# for i in range(n):
#     v=1
#     for j in range(n):
#         if i%2==0:
#             print(v,end=" ")
#             v+=1
#         else:
#             print("*",end=" ")
#     print()
'''
A B C D E
* * * * *
A B C D E
* * * * *
A B C D E
'''

'''
1 * 3 * 5
1 * 3 * 5
1 * 3 * 5
1 * 3 * 5
1 * 3 * 5_
'''
# n=5
# for i in range(n):
#     for j in range(1,n+1):
#         if j%2!=0:
#             print(j,end=" ")
#         else:
#             print("*",end=" ")
#     print()
n=5
for i in range(n):
    v=1
    for j in range(n):
        if j%2==0:
            print(v,end=" ")
        else:
            print("*",end=" ")
        v+=1
    print()