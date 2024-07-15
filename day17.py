'''
        *
      * *
    * * *
  * * * *
* * * * *
'''
# n=5
# for i in range(n):
#     for j in range(n):
#         if i+j>=n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
    
#1st 
# n=5
# val=1
# for i in range(n):
#     for j in range(n):
#         if val == 10:
#             val=1
#         if i+j>=n-1:
#              print(val,end=" ")
#              val+=1
#         else:
#             print(" ",end=" ")
#     print()

#2 
# n=5
# for i in range(n):
#     for j in range(n):
#         if i+j>=n-1:
#             if j%2!=0:
#                 if j==3:
#                     print(1,end=" ")
#                 else:
#                     print(2,end=" ")
#             else:
#                 print("*",end=" ")      
#         else:
#             print(" ",end=" ")
#     print()


# 3
# n=5
# for i in range(n):
#     for j in range(n):
#         if i+j>=n-1:
#             if i%2==0:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=5 
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
    
# n=5 
# for i in range(n):
#     for j in range(n):
#         if i+j<=n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==j or i+j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=5
# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#       if i+j<=n+1:
#         if j%2!=0:
#             print("*",end= " ")
#         else:
#             print(j//2,end= " ")
#       else:
#         print(" ",end=" ")
#     print() 
    
# n=5
# for i in range(n,0,-1):
#   for j in range(n,0,-1):
#     if i+j<=n+1:
#       if j%2==0:
#         print(j//2,end=" ")
#       else:
#         print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()
  
  
# n=15
# for i in range(n):
#   for j in range(n):
#     if i==0 or i==n-1 or j==0 or j==n-1 or i+j==n-1 or i==j:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()
  
  
# n=5
# for i in range(n):
#   for j in range(n):
#     if i==n//2 and j==n//2:
#       print("Hi",end= " ")
#     else:
#       print(" ",end=" ")
#   print()
  
# n=5
# for i in range(n):
#   for j in range(n):
#     if i==j or i+j==n-1:
#       if i==j and i+j==n-1:
#         print("S",end=" ")
#       else:
#         print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()

# n=5
# for i in range(n):
#   for j in range(n):
#     if i==0 or i==n-1 or j ==0 or j==n-1 or i==j or i+j==n-1:
#       if i==j and i+j==n-1:
#         print("S",end=" ")
#       else:
#         print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()
  
# n=5 
# for i in range(n):
#   for j in range(n):
#     if i+j==n-1 or i==n-1:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()
  
# n=5 
# for i in range(n):
#   for j in range(n):
#     if i+j==n-1 or i==0:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()
  
# n=5 
# for i in range(n):
#   for j in range(n):
#     if i==n-1 or i==j:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()

# n=5 
# for i in range(n):
#   for j in range(n):
#     if i==0 or i==n-1 or i+j==n-1:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()

n=5
for i in range(n):
  for j in range(n):
    if i==0:
      print("*",end=" ")
    elif j==n-1:
      print(1,end=" ")
    else:
      print(" ",end=" ")
  print()