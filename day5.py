# # wap to check whether the char is uppercase,lowercase,digit,special character.
# char = input()
# if 'A'<=char<='Z':
#     print('Upper Case')
# elif 'a'<=char<='z':
#     print('Lower Case')
# elif '0'<=char<='9':
#     print('Its Digit')
# else:
#     print('Special Char')
# # wap to check whether the given integer is 1digit,2digit,3digit.
# n = int(input())
# if -9<=n<=9:
#     print('1 Digit')
# elif -99<=n<=-10 or 10<=n<=999:
#     print('2 Digit')
# elif -999<=n<=-100 or 100<=n<999:
#     print('3 DIGIT')
# else:
#     print('More than 3 Digit')
    
# # wap to check given points are lying in which quadrant.
# n1 = int(input())
# n2 = int(input())
# if n1>0 and n2>0:
#     print(f'both {n1} and {n2} is 1st quadrant')
# elif n1>0 and n2<0:
#     print(f'{n1} and {n2} is in 2nd quadrant')
# elif n1<0 and n2<0:
#     print(f'{n1} and {n2} is in 3rd quadrant')
# else:
#     if n1==0 or n2==0:
#         print('Zero invalid')
#     else:
#         print(f'{n1} and {n2} is in 4th quadrant')
    
# # wap to print the last value of a list only if it is having a palindrome when string starting with vowel.
# # method 1
# l = eval(input())
# if type(l[-1]) == str:
#     if l[-1]==l[-1][::-1]:
#         if l[-1][0] in 'AEIOUaeiuo':
#             print(f'{l[-1]}')
#         else:
#             print(f"{l[-1]} is not a vowel")
#     else:
#         print("Not a palindrome")
# else:
#     print("not a string type")
    
# #method 2
# l = eval(input())
# if (type(l[-1]) == str) and (l[-1]==l[-1][::-1]) and (l[-1][0] in 'AEIOUaeiuo'):
#     print(l[-1])
# else:
#     print(f"{l[-1]} is not valid")
    
# wap consider a character input is uppercase then convert into lowercase,if lowercase convert into uppercase,if digit multiply by 3 rem get the remainder ,if it is spl character print ascii values. 
 
# print(ord('A')-ord('a'))
# char= 'A'
# print(chr((ord(char))+32))
# char1 = 'a'
# print(chr((ord(char1))-32))
# char2='9'
# print(int(char2)%3)
# char3 = '@'
# print(ord(char3))

# char = input()
# if 'A'<=char<='Z':
#     print(chr((ord(char))+32))
# elif 'a'<=char<='z':
#     print(chr((ord(char))-32))
# elif '0'<=char<='9':
#     print(int(char)%3)
# else:
#     print(ord(char))

