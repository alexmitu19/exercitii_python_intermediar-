########### built-in decorator ##########
from functools import lru_cache

@lru_cache(maxsize=100) # lru - least recently used
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(496))


#@lru_cache(maxsize=50)
def print_fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        print(a)
        aux = a
        a = b
        b = aux+b

print_fibonacci(10)

'''
a,b = b, a+b ===== aux = a , a=b , b = aux+b
a,b = b , a+b != a = b, b = a + b
'''