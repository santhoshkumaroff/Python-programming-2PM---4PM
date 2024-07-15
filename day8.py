# prime number 

# #method 2

n = int(input())
i=2
count = 0
while i<=n//2:
    if n%i==0:
        count =1
    i+=1

if count==0 and n!=1:
    print('Prime ')
else:
    print('Not a Prime')

# wap to print fibonacci series
# method 1
# n=int(input("Enter Number : "))
# start =0
# prev = 1
# next = 0
# while n>0:
#     print(next,end=" ")
#     start,prev=prev,next
#     next = start+prev
#     n-=1

# method 2
# n=int(input("Enter Number : "))-2
# l=[0,1]
# while n>0:
#     next = l[-1]+l[-2]
#     l+=[next]
#     n-=1
# print(l)

#wap to find factorial of given number

# n = int(input("Enter Number"))
# fact = 1
# while n>0:
#     fact=fact*n 
#     n-=1
# print(fact)

# wap to find given number is strong number or not.

# n = int(input("Enter Number : "))
# sum=0
# while n!=0:
#     ld = n%10
#     fact = 1
#     while ld>0:
#         fact = fact*ld #or fact*=ld
#         ld-=1
#     sum+=fact
#     n=n//10 #or n//=10
# print(sum)

# wap to find the given number is amstrong or not.


# n=int(input("Enter Nmber"))
# l = len(str(n))
# sum=0
# while n!=0:
#     ld = n%10
#     sum+=ld**l
#     n//=10
# print(sum)

# guessing number
# import random
# random_number = random.randint(1,100)
# while True:
#     guessing_number = int(input("Enter Number"))
#     if guessing_number>random_number:
#         print(f"Your {guessing_number} is greater than random number")
#     elif guessing_number<random_number:
#         print(f'Your {guessing_number} is lower than random number')
#     else:
#         print(f"Yes You Entered Correct number {random_number}")
#         break