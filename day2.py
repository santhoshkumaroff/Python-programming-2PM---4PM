# # 1
# num = int(input())
# if num%10==5:
#     print("Yes")

# #2
# #method 1
# num1=int(input())
# if (num1>=100 and num1<=999) or (num1>=-999 and num1<=-100):
#     print("Its a 3 digit")
# # method 2 
# num2 = int(input())
# if 100<=num2<=999 or -999<=num2<=-100:
#     print("It's a three digit")

#3
# data = eval(input())
# data = float(input())
# if type(data)==float:
#     print("yes")

# #wap to check the given data is single value data.
# data = eval(input())
# if type(data) in [int,float,complex,bool]:
#     print("Yes")
    
#wap to check whether the given char is digit.
# char = input()
# if '0'<=char<='9':
#     print("Yes")

char = 'A'
print(ord('0'),ord('5'),ord('9'))

# wap to check whether the given interger is multiple by both 5 and 3.

num = int(input())
if num%3==0 and num%5==0:
    print("Yes")
