# # wap to check the age of a person and print a different message.
# # age>=60 - senior citizen,age >=18 - adult,age<18 - teenager

# age = int(input("Enter age"))
# if age>=60:
#     print("Senior citizen")
# else:
#     if age>=18:
#         print('Adult')
#     else:
#         print('Teenager')
        
# # 
# n1=int(input())
# n2=int(input())
# option = int(input("Enter option : "))
# if option ==1:
#     print(f"add = {n1+n2}")
# elif option==2:
#     print(f"sub - {n1-n2}")
# elif option == 3:
#     print(f"mul {n1*n2}")
# elif option == 4:
#     print(f"div {n1/n2}")
# elif option == 5:
#     print(f"pow {n1**n2}")
# else:
#     print("Invalid option")
# # 
# balance = 100000
# option = int(input())
# if option ==1:
#     print(f"balance : {balance}")
# elif option ==2:
#     d_amt = int(input())
#     print(f"current balance is {balance+d_amt}")
# elif option == 3:
#     w_amt = int(input())
#     print(f"Current balance is {balance-w_amt}")
# else:
#     print("Invalid Option..")
    
# wap to print all charcters of string.

# wap to extract all the lowercase,uppercase,digit,special char from the given string.
# string = "HeLlo@123"
# i = 0
# l_case=''
# up_case=''
# digit = ''
# splchar = ''
# while i<len(string):
#     if 'a'<=string[i]<='z':
#         l_case+=string[i]
#     elif 'A'<=string[i]<='Z':
#         up_case+=string[i]
#     elif '0'<=string[i]<='9':
#         digit+=string[i]
#     else:
#         splchar+=string[i]
#     i+=1

# n = int(input())
# i=1
# while i<n:
#     if n%i==0:
#         print(i,end=" ")
#     i+=1
# rev=0
# n = int(input())
# while n!=0:
#     ld = n%10
#     rev = rev*10+ld
#     n//=10
# print(rev)

string = "HeLlo@123"
i = 0
output = ''
while i<len(string):
    if 'a'<=string[i]<='z':
        output +=chr(ord(string[i])-32)
    elif 'A'<=string[i]<='Z':
        output +=chr(ord(string[i])+32)
    elif '0'<=string[i]<='9':
        output+= string[i]
    else:
        output+= string[i]
    i+=1
print(f"String : {string}\nReversed string : {output}")