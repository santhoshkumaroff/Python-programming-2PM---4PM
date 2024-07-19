#perfect number
def perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum ==n
# l=[i for i in range(1,50) if perfect(i)]
# print(*l)
#checkprime
def checkprime(n):
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l+=[i]
    return len(l)==2
#amstrong
def amstrong(n):
    sum=0
    for i in str(n):
        sum+=int(i)**len(str(n))
    return sum==n
def hcf(n1,n2):
    hcf=0
    for i in range(1,min(n1,n2)+1):
        if n1%i==0 and n2%i==0:
            hcf=i
    return hcf
# n1=int(input("Enter n1 : "))
# n2=int(input("Enter n2 : "))
# print(f"Lcm of {n1} and {n2} is {n1*n2//hcf(n1,n2)}")

#normal method
# def fact(n):
    # fact=1
    # for i in range(n,0,-1):
    #     fact*=i
    # return fact
#factorial
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
# print(fact(3))
#strongnumber
def strong(n):
    sum=0
    for i in str(n):
        sum+=fact(int(i))
    return n==sum
# print(strong(10))

# for i in range(1,500):
#     if strong(i):
#         print(i,end=" ")
        
# print(*[i for i in range(1,500) if strong(i)])

def numberslogic():
    option = int(input('1. check prime\n2. amstrong\n3. Factorial\n4.Strong\n5.Perfect\nEnter Your Option : '))
    match option:
        case 1:
            print(checkprime(int(input("Enter number : "))))
        case 2:
            print(amstrong(int(input("Enter number : "))))
        case 3:
            print(fact(int(input("Enter number : "))))
        case 4:
            print(strong(int(input("Enter number : "))))
        case 5:
            print(perfect(int(input("Enter number : "))))
        case _:
            print("Invalid Option")
            numberslogic()
numberslogic()

# https://github.com/santhoshkumaroff/Python-programming-2PM---4PM

