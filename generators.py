# Generators and Iterators

a = [1, 2, 3, 4]
for i in a:
    pass
    # print(i)

b = "eu sunt daniel"
for c in b:
    pass
    # print(c)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

from collections.abc import Iterator
class PrimeIterator(Iterator):
    def __init__(self, n):
        self.n = n
        self.generated_numbers = 0
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.generated_numbers >= self.n:
            raise StopIteration
        elif is_prime(self.number):
            self.generated_numbers += 1
            return self.number
        return self.__next__()


iter = PrimeIterator(9)
for elem in iter:
    print(elem)

def prime_generator(n):
    number = 2
    generated_numbers = 0
    while generated_numbers != n:
        if is_prime(number):
            yield number
            generated_numbers += 1
        number += 1

gen = prime_generator(1000)
for elem in gen:
    print(elem)