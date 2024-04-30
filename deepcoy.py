
from copy import deepcopy
class Simplu:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self): #  spune lui print cum sa il afiseza membri
        return f'{self.a} si {self.b}'

s = Simplu(5, 7)

lista =[1, s, 'abc']
shallow_list_copied = list(lista)
deep_list_copied = deepcopy(lista)

lista[0] = 2
lista[1].a = 3

print(lista, shallow_list_copied, deep_list_copied)
