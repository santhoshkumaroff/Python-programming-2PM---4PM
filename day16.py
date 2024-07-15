# n=5
# val=1
# for i in range(n):
#     for j in range(n):
#         if val==10:
#             val=1
#         if i>=j:
#             print(val,end=" ")
#             val+=1
#         else:
#             print(" ",end=" ")
#     print()

# n=5
# val=1
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             if i%2==0:
#                 print(val,end=" ")
#                 val+=1
#             else:
#                 print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
    

# n=5
# for i in range(n):
#     for j in range(n):
#         if i+j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
    
# n=5
# val=0
# for i in range(n):
#     for j in range(n):
#         if i+j ==n-1:
#             print(chr(65+i),end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=5
# val=1
# for i in range(n):
#     for j in range(n):
#         if i+j==n-1:
#             if i%2==0:
#                 print(val,end=" ")
#                 val+=1
#             else:
#                 print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
    
# n=7
# val=n//2
# for i in range(n):
#     for j in range(n):
#         if i+j==n-1:
#             if i%2==0:
#                 print(chr(65+val),end=" ")
#                 val-=1
#             else:
#                 print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()