# # # # # # # s = 'Hello'
# # # # # # # i=0
# # # # # # # rev=''
# # # # # # # while i<len(s):
# # # # # # #     rev=s[i]+rev
# # # # # # #     i+=1
# # # # # # # print(rev)

# # 
# l=['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
# s = input("Enter number")
# i=0
# # print(s,s[0])
# while i<len(s):
#     # print(i)
#     char=s[i]
#     int_char= int(char)
#     # print(1,char,int_char,l[int_char])
#     print(l[int(s[i])],end=' ')
#     i+=1


# # # # # # wap to run infinite loop to login phonepa if entered otp is correct and print 'Login successfull '.
# # # # # import random
# # # # # # print(otp)
# # # # # while True:
# # # # #     otp = random.randint(1000,9999)
# # # # #     u_otp = int(input(f'your otp is {otp}\nEnter OTP : '))
# # # # #     if otp == u_otp:
# # # # #         print('Login')
# # # # #         break
# # # # #     else:
# # # # #         print('Wrong OTP ❌❌❌\nEnter again👇👇')

        
# # # # username = 'Hello123'
# # # # password = 'Pass@123'

# # # # while True:
# # # #     u_user = input()
# # # #     if u_user==username:
# # # #         u_pass = input()
# # # #         if u_pass == password:
# # # #             print('Login...✅✅✅')
# # # #             break
# # # #         else:
# # # #             print('Wrong password\nEnter Again')
# # # #     else:
# # # #         print('Username invalid')

# # # pos=''
# # # neg=''
# # # while True:
# # #     n=int(input())
# # #     if n>0:
# # #         pos+=f'{str(n)} '
# # #     elif n<0:
# # #         neg+=f'{str(n)} '
# # #     else:
# # #         print(f"You entered {n}")
# # #         break
# # # print(f'pos : {pos}\n Neg : {neg}')
# # #method 1
# # n = int(input())
# # i=1
# # prime = []
# # while i<=n:
# #     if n%i==0:
# #         prime.append(i)
# #     i+=1
# # # print(prime,len(prime))
# # if len(prime)==2:
# #     print('Prime number')
# # else:
# #     print('Not a prime number')

# # #method 2

# # n = int(input())
# # i=2
# # count = 0
# # while i<=n//2:
# #     if n%i==0:
# #         count =1
# #     i+=1

# # if count==0 and n!=1:
# #     print('Prime ')
# # else:
# #     print('Not a Prime')

# # wap to print fibonacci series
# # method 1
# # n=int(input("Enter Number : "))
# # start =0
# # prev = 1
# # next = 0
# # while n>0:
# #     print(next,end=" ")
# #     start,prev=prev,next
# #     next = start+prev
# #     n-=1

# # method 2
# # n=int(input("Enter Number : "))-2
# # l=[0,1]
# # while n>0:
# #     next = l[-1]+l[-2]
# #     l+=[next]
# #     n-=1
# # print(l)

# #wap to find factorial of given number

# # n = int(input("Enter Number"))
# # fact = 1
# # while n>0:
# #     fact=fact*n 
# #     n-=1
# # print(fact)

# # wap to find given number is strong number or not.

# # n = int(input("Enter Number : "))
# # sum=0
# # while n!=0:
# #     ld = n%10
# #     fact = 1
# #     while ld>0:
# #         fact = fact*ld #or fact*=ld
# #         ld-=1
# #     sum+=fact
# #     n=n//10 #or n//=10
# # print(sum)

# # wap to find the given number is amstrong or not.


# # n=int(input("Enter Nmber"))
# # l = len(str(n))
# # sum=0
# # while n!=0:
# #     ld = n%10
# #     sum+=ld**l
# #     n//=10
# # print(sum)

# # guessing number
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