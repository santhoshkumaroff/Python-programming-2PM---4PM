# wap to check whether the data is mutable or not.
# list,set,dict
# data = eval(input())
# # print(data,type(data))
# if type(data) in [list,set,dict]:
#     print("Mutable")
# else:
#     print("Immutable")

#wap to check the given char is special character or not.

# char= input()
# # method 1
# print('A'<=char<'Z','a'<=char<='z','0'<=char<='9') 
# if ('A'<=char<'Z' or 'a'<=char<='z' or '0'<=char<='9'):
#     print("Not a special char")
# else:
#     print('special char')
    
# # method 2
# if not('A'<=char<'Z' or 'a'<=char<='z' or '0'<=char<='9'):
#     print("special char")
# else:
#     print('Not a special char')
    
# wap to check whether a list consits of middle value or not.
# l1 = [1,3,4,5]
# l2 = [10,20,30,40,50]

# # print("check ",len(l1)%2==0,len(l2)%2==0)
# if len(l2)%2==0:
#     print("Not have")
# else:
#     print(f"Yes {l2} having middle value {l2[len(l2)//2]}")
    
# wap to to check give char is upper case or lower case

# wap to check whether the given two variable is pointing same address or not.

# use id() or identity(is,is not)

# a=int(input())
# b = int(input())
# # method 1

# if a is b:
#     print(f"yes {a} and {b} is pointing same address")
# else:
#     print("not matching")
# # method 2

# if id(a) == id(b):
#     print("Yes")
# else:
#     print("No")
    
# consider a tuple of length 2 and check tuple is homogeneous or heterogeneous
