# for i in range(n):
#     for j in range(n):
#         if j==0 or j==n-1 or (i==j and i<=n//2) or (i+j==n-1 and i<=n//2):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
    
    
    
    
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n//2 or i==n-1 or (j==0 and i<=n//2) or (j==n-1 and i>=n//2):
#             print("*",end=" ")
#         else:
#             print(" ",end= " ")
#     print()


# n=5 #1
# for row in range(n):
#     for space in range(n-row-1):
#         print(" ",end=" ")
#     for star in range(2*row+1):
#         # if star%2==0:
#             print("*",end=" ")
#         # else:
#         #     print(" ",end=" ")
#     print()
# n=5#1
# for i in range(n): #2
#     print("  "*(n-i-1)+'* '*(2*i+1))

n=5
# for i in range(n,0,-1):
#     for space in range(n-i):
#         print(" ",end=" ")
#     for star in range(2*i-1):
#         print("*",end=" ")
#     print()
    
# for i in range(n,0,-1):
#     print("  "*(n-i)+"* "*(2*i-1))