n=int(input("Enter a number: "))
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
print(f"The factorial of {n} is {factorial(n)}")



l=list(map(int,input("Enter a list of numbers separated by spaces: ").split()))
print(f"List: {l}")
def mean(l):
    return sum(l)/len(l)
print(f"average: {mean(l)}")


def square_list(*args):
    return sum(i**2 for i in args)

print(square_list(1,2,3,4,5))