#1) WAP to print the square of a number only if it is even

'''
method 1

n=int(input('Enter a value: '))
if n%2==0:
    print('square is: ',n**2)

method 2

n=int(input('Enter a value: '))
if (n//2)*2==0: # n&1==0 # n|1==n+1
    print('square is: ',n**2)
'''

#2) WAP to check whether the character is vowel or not.

'''s=input('Enter a char : ')
if s in 'aeiouAEIOU':
    print('VOWEL')'''


#3)wap to print ascii value of a character only if
#it is uppercase without using inbuilt functions..

'''

method 1

ch=input('Enter a char: ')
if 'A'<=ch<='Z':
    print('ASCII val is: ',ord(ch))

method 2

ch=input('Enter a char: ')
if ch>='A' and ch<='Z':
    print('ASCII val is: ',ord(ch))

'''

#4)WAP to print the cube of a number only if it is
#divisible by 9 or 6.

'''
n=int(input('Enter a num: '))
if n%9==0 or n%6==0:
    print('Cube is: ',n**3)
'''