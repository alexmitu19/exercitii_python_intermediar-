'''
Lambda expressions:

def numele_functiei(a,b,c):
    #
    :return

lambda expression : functie anonima, care nu are nume, este definita acolo unde este utilizata

lambda ...

'''

continut = lambda x: x.lower()

print(continut("JAJAJA"))
'''
echivalent cu:
def continut(x):
    return x.lower()

'''

lista_numere = [1, 2, 3, 4, 5]

# map : accepta o functie si o aplica pe fiecare element al unui obiect iterabil ( lista..)

lista_squared = list(map(lambda x: x ** 2, lista_numere))
print(lista_squared)

# filter : sterge elementele pentru care rezultatul functiei aplicate returneaza False

lista_impare = list(filter(lambda x: x % 2, lista_squared))
print(lista_impare)

# reduce : proceseaza toate elementele dintr-un obiect iterabil de la stanga la dreapta(!) si produce o singura valoare
# in functie de functia aplicata

from functools import reduce

item_sumati = reduce(lambda x, y: x + y, lista_impare)
print(item_sumati)

# [1, 9, 25] -> reduce -> ((1,9), 25) -> (1+9), 25 -> (10,25) -> (10+25) -> 35

# MapReduce -> parcurge o lista imensa / baza de date : sa aplice o functie pt fiecare element, apoi sa reduca intregul
# tabel la o singura valoare
'''
4 5 1 7 8 9 12 45 90
5 6 23 3 5 6 3 3 2 2   -> Map ( functie mediere ) -> Reduce ( per celula ) -> tabel mai mic ca dimensiune si mai usor de procesat
1 4 5 3 562 2 2 4 6 7
'''

# sorted, max , min

# sorted -> va aranjeaza/sorteaza in ordine elementele

perechi = [(1, 9), (4, 6), (5, 3)]

print(sorted(perechi, reverse=True))

print(max(perechi, key=lambda x: x[0] * x[1]))


# Enunt exercitiu : creati o functie care verifica daca un nr este prim
# apoi dintr-o lista filtrati numerele prime folosind filter()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


lista_numere2 = [5, 6, 11, 23, 27, 73, 56, 81]
lista_numere_prime = list(filter(is_prime, lista_numere2))
print(lista_numere_prime)