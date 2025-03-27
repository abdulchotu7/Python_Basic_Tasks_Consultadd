n=int(input())
if n<=0:
    print("Enter a positive integer.")
    exit()
if n%2==0:
    print("Even")
elif n%2==1:
    print("Odd")
def is_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
if is_prime(n):
    print("Prime")