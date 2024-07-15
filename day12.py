# wap to convert binary to decimal values.
# n=1111
# sum =0
# p=0
# for i in str(n)[::-1]:
#     sum+=int(i)*2**p
#     p+=1
# print(sum)

# wap to convert decimal to binary values

# n=15
# out =''
# for i in range(n): #0 #1 #2 #3
#     if n!=0:
#         rem = n%2 # 1 #7%2=> 1 3%2 => 1 #1%2 => 1
#         out = str(rem) + out #1 -> '1'+ '' => '1' # 1->'1'+'1' => '11' # 1 => '1' + '11'=>'111' #1-> '1'+'111'=>'1111'
#         n//=2 # n=n//2 15//=2 #7//=2 => 3//=2=> 1//=2 => 0
#     else:
#         break
# print(out)

# wap to find super digit of a given number.

n= 546893 # 35
while len(str(n))!=1: # len("546893")=>6!=1 #len("35")!=1
    sum=0 #0 # 35 #0
    for i in str(n): # for i in "546893"
        sum+=int(i) # sum = 0+5=>5+4 => 9+6=>15+8=>23+9=> 32+3 => 35
    print(n,sum)
    n=sum # updating the sum value to n
