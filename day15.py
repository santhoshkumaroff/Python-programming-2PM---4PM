'''
* * 1 * * 
* * 1 * * 
* * 1 * * 
* * 1 * * 
* * 1 * * 
'''
# n=5
#method 1
# for i in range(n): # 0 1 2 3 4
#     for j in range(n): # 0 1 2 3 4
#         if j == n//2:
#             print("1",end=" ")
#         else:
#             print("*",end=" ")
#     print()
    
# # method 2
# for i in range(1,n+1): #  1 2 3 4 5
#     for j in range(1,n+1): # 1 2 3 4 5
#         if j == (n//2)+1:
#             print("1",end=" ")
#         else:
#             print("*",end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(n):
#         if j==n//2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

'''
* * * * *
* * * * *
1 2 3 4 5
* * * * *
* * * * *
'''
# n=5
# val=1
# for i in range(n):
#     for j in range(n):
#         if i ==n//2:
#             print(val,end=" ")
#             val+=1
#         else:
#             print("*",end=" ")
#     print()

# n=5
# val=1
# for i in range(n):
#     for j in range(n):
#         if i ==n//2:
#             print(val,end=" ")
#             val+=1
#         else:
#             print(" ",end=" ")
#     print()
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==n//2 or j==n//2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==n//2 and j==n//2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
    
# 1
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print("0",end=" ")
#         else:
#             print("1",end=" ")
#     print()
    
# 2 
# n=5
# val=0
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print(chr(65+val),end=" ")
#             val+=1
#         else:
#             print("*",end=" ")
#     print()
    
n=5
for i in range(n):
    for j in range(n):
        if i>=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()