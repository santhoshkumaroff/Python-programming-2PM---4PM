#lamda filter map

#lambda example
def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return n>1
# print(prime(1))
is_prime = lambda num : num>1 and all(num%i!=0 for i in range(2,(num//2)+1))
# print(is_prime(5))
#amstrong 
'''
sum=0
for i in str(num):
    sum+=int(i)**len(str(num))
'''
#amstrong number
amstrong = lambda num : num == sum(int(i)**len(str(num)) for i in str(num))
# print(amstrong(153))


#filter 

#square of nums #map
# def square(num):
#     return num*num
# nums=[1,4,6,8,2]
# values = list(map(lambda n: n*n,nums))

#method 1
# print(*values)
#method 2
# print(values)

#return nums should be greater than 2
# nums=[1,2,3,45,67,45]

# values = list(filter(lambda n :n%2,nums))
# print(values)

# rangeprimenums = list(filter(amstrong, range(1,1000)))
# print(rangeprimenums)

'''
i/p = ["Today","Is","Monday"]
o/p = ["ydT","I","anM"]
'''

words = ["Today","Is","Monday"]
values = list(map(lambda words: words[::2][::-1], words))
print(values)
'''

i/p:  words = ["Today","Is","Monday"]
o/p : ["today : 5" ,"Is: 2","Monday : 5"]
'''
