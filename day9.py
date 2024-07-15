# i/p : ['hai','Hello','Good']
# l= ['hai','Hello','Good']
# i=0
# out = {}
# while i<len(l):
#     out[l[i]] = len(l[i])
#     i+=1
# print(out)

# i/p : l = ["Hello",38,14.5,"good","Bye","py",(1+6j)]
#
# l = ["Hello",38,14.5,"good","Bye","py",(1+6j)]
# out = {}
# i= 0
# while i<len(l):
#     if type(l[i])==str:
#         out[l[i]]= l[i][0]+l[i][-1]
#     i+=1
# print(out)

# i/p = "Hello Hai"
# o/p : "iaH olleH"


# find odd or even in a single line without using if and for loop.
# print(['Even','odd'][int(input("Enter Number : "))%2])

# 
# n = int(input("Enter Number to ask input : "))
# i=1
# sum=0
# while i<=n:
#     u_num = int(input(f"N {i} : "))
#     sum+=u_num
#     i+=1
# print(sum/n)

# wap to convert decimal to binary values

n = int(input("Enter Decimal Value : "))
s= ' '
while n!=0:
    rem = n%2
    s = str(rem)+s
    n//=2 # or n= n//2
print(s)

# wap to convert binary to decimal values.
# n = int(input("Enter Binary Value : "))
# sum=0
# pow=0
# while n!=0:
#     rem = n%10
#     sum += rem*2**pow
#     pow+=1
#     n//=10
# print(sum) 