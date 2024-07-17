def perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum ==n
# l=[i for i in range(1,50) if perfect(i)]
# print(*l)

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
    fact=1
    for i in range(n,0,-1):
        fact*=i
    return fact
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(6))