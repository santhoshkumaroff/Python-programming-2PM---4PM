
# write a program to find gcd of 2 numbers

# n1 = int(input("Enter number 1 : "))
# n2 = int(input("Enter number 2 : "))
# i=1
# endvalue = max(n1,n2)
# gcd = 0
# while i<=endvalue:
#     if n1%i==0 and n2%i==0:
#         gcd =i
#     print(i)
#     i+=1
# print(f"The gcd of {n1} and {n2} is {gcd}")
    
# write a program to find lcm of 2 number.

# n1 = int(input("Enter number 1 : "))
# n2 = int(input("Enter number 2 : "))
# maxvalue = max(n1,n2)
# lcm=0
# upt_value = maxvalue
# while True:
#     if maxvalue%n1==0 and maxvalue%n2 ==0:
#         lcm=maxvalue
#         break
#     maxvalue+=upt_value
# print(lcm)

# write a program to check whether the given list is homogeneous or heterogeneous.
# l = ['Cricket',15.76,'Football',13]
l = ['Cricket','Football',155]
for i in l:
    if type(l[0]) != type(i):
        print("Heterogeneous")
        break
else:
    print("Homogeneous")

# wap to remove duplicate values in a list without using any inbuilt condition.

l = [10,20,30,10]
out=[]
for i in l:
    if i  not in out:
        out+=[i]
        
print(out)

#wap to split the string without using split function.
s = " Hello Hi  "
emp_strv=""
out = []
for i in s:
    if i!= " ":
        emp_strv+=i
    else:
        out+=[emp_strv]
        emp_strv=""
# else:
#     out+=[emp_strv]
print(out)
removed_list =[]
for i in out:
    if i !="":
        removed_list+=[i]
print(out,removed_list)