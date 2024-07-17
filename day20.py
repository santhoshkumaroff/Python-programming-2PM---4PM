def checkprime(n):
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l+=[i]
    if len(l)==2:
        return True
    return False
# print(checkprime(3))
# for i in range(5,30):
#     if checkprime(i):
#         print(i,end=" ")
        
def amstrong(n):
    sum=0
    for i in str(n):
        sum+=int(i)**len(str(n))
    return sum==n
# print(amstrong(150))
# for i in range(140,180):
#     if amstrong(i):
#         print(i,end=" ")
