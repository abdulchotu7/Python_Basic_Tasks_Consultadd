def prime_numbers_up_to_50():
    for num in range(2, 51):  
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):  
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num  

for prime in prime_numbers_up_to_50():
    print(prime)
print("----")

# def infinite_count():
#     num = 2
#     while True:
#         yield num
#         num += 1

# gen = infinite_count()
# while True:
#     print(next(gen))

class FibonacciIterator:
    def __init__(self, n):
        self.n = n  
        self.current = 0  
        self.next = 1  
        self.count = 0  

    def __iter__(self):
        return self  

    def __next__(self):
        if self.count >= self.n:  
            raise StopIteration
        fib = self.current
        self.current, self.next = self.next, self.current + self.next
        self.count += 1
        return fib

n = 10  
fib = FibonacciIterator(n)
for i in fib:
    print(i)
