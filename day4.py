#  wap to check whether the given string is palindrome or not.
# string = input()
# if string == string[::-1]:
#     print("Palindrome")
# else:
#     print("Not a Palindrome ..")

# wap to check the given number is +ve or -ve.

# num = int(input())
# if num>0:
#     print("+ve")
# else:
#     print('-ve')
    
'''Nested if '''

# wap to login into instagram with valid username,password only if username is valid.

# username ='abcd'
# password = 'abc@123'
# u_name = input("Enter user name : ")
# if username == u_name:
#     u_password = input("Enter password  ")
#     if password == u_password:
#         print("Login....")
#     else:
#         print("Password not matching..")
# else:
#     print("Username is not matching...")

# wap to print the middle value of list only it is string.

#method 1
# l = [1,2,3,"dhoni",3,4,5]
# method 2
# l1 = list(input())
# print(l1)
# # print(l[len(l)//2])
# if len(l1)%2!=0:
#     # l[len(1)//2]
#     if type(l1[len(l1)//2]) == str:
#         print(f"The middle value is {l1[len(l1)//2]}")
#     else:
#         print("Middle value is not a string")
# else:
#     print("Not having middle value")


# wap to check the give character is vowel or consonant.

# char = input()
# if 'A'<=char<='Z' or 'a'<=char<='z':
#     if char in 'AEIOUaeiou':
#         print(f"Yes {char} is vowel")
#     else:
#         print(f"{char} is consonant")
# else:
#     print("The given char is not an alphabet")


# # wap to find the length of the given data only if it is list.
# data  = eval(input())
# if type(data) in [str,list,tuple,set,dict]:    
#     if type(data) == list:
#         print(f"the length os list is {len(data)}")
#     else:
#         print("Not list type")
# else:
#     print("Not MVD")


# # wap to check greatest of two number. 
# n1 = int(input())
# n2 = int(input())
# if n1>n2:
#     print(f"{n1} is greater than {n2}")
# else:
#     print(f"{n2} is greater than {n1}")
# # wap to check greatest of three number.
# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
# if n1>n2 and n1>n3:
#     print(f'{n1} is greater than {n2} and {n3}')
# elif n2>n3:
#     print(f"{n2} is greater than both {n1} and {n2}")
# else:
#     print(f"{n3} is greater than both {n1} and {n2}")
    
# # wap to check second greatest of three number.

# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
# if n1>n2 and n1>n3:
#     if n2>n3:
#         print(f"{n2} is second greatest")
#     else:
#         print(f"{n3} is second greatest")
# elif n2>n3:
#     if n1>n3:
#         print(f"{n1} is second greatest")
#     else:
#         print(f"{n3} is second greatest")
# else:
#     if n1>n2:
#         print(f"{n1} is second greatest")
#     else:
#         print(f'{n2} is second greatest')

    