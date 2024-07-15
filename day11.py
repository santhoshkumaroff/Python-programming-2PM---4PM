# wap to check the given number is prime or not.

# n= int(input("Enter Number : "))
# l=[]
# for i in range(1,n+1):
#     if n%i==0:
#         l+=[i] # l.append(i)
# if len(l)==2:
#     print("Prime number") #TSB
# else:
#     print("Not a prime") # FSB

# print("Prime number") if len(l)==2 else print("Not a prime") 

#method 2

# wap to find factorial of given number

# n=int(input("Enter number : "))
# fact = 1
# for i in range(n,0,-1):
#     fact=fact*i # fact*=i
# print(fact)
# wap to check the number is strong number or not only by using for loop.

# n = 145
# sum=0
# for i in str(n):
#     fact=1
#     for i in range(int(i),0,-1):
#         fact*=i
#     sum+=fact
# print(sum==n)

# wap to check given number is amstrong or not.
n=153
sum=0
for i in str(n):
    sum+=int(i)**len(str(n))
print(sum==n)
# wap to check the given number is perfect or not.
n=6
sum=0
for i in range(1,n//2+1):
    if n%i==0:
        sum+=i
# print(6)
print("Perfect") if sum==n else print("Not a perfect")

# wap to find hcf of 2 numbers
n1 = int(input("Enter number 1 : "))
n2 = int(input("Enter number 2 : "))
hcf = 0
for i in range(1,min(n1,n2)+1):
    if n1%i==0 and n2%i==0:
        hcf=i
    print(i,end=" ")
print(hcf)
