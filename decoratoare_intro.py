## Decoratorul este o functie care imbraca o alta functie si ii extinde functionalitatea. Intotdeaduna este precedat de '@'.
# O functie ia ca argument alta functie.
# Intr-o functie se poate crea alta functie: functii imbricate.

from datetime import datetime


def disabled_at_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 21:
            func()
    return wrapper

@disabled_at_night
def ceva():
    print("Hhhhh")

ceva()

########### built-in decorator ##########
from functools import lru_cache

@lru_cache(maxsize=100) # lru - least recently used
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(496))

