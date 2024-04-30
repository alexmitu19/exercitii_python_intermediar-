### OOP - object oriented programming : Python (totul este un obiect)
### functionale: Lisp, Haskell > aproape toate operatiile sunt functii
### high-level, strongly typed : C, C++ ( a = 5 -> int a = 5; )
# init sau str se numesc dumber methods
# OOP - mostenirea
class Persoana:  # clasa de baza
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def __str__(self):
        return f"{self.nume} are varsta {self.varsta}"


class Angajat(Persoana):  # clasa mostenita ( clasa copil ) -> mosteneste init si str
    def __init__(self, nume, varsta, salariu, ore_lucrate):
        super().__init__(nume, varsta)  # super() -> adica superclass : clasa din care mostenim
        self.salariu = salariu
        self.ore_lucrate = ore_lucrate

    def arata_finante(self):
        return self.salariu * self.ore_lucrate


class Student(Persoana):  # clasa copil > mosteneste init si str
    def __init__(self, nume, varsta, bursa):
        super().__init__(nume, varsta)
        self.bursa = bursa

    def arata_finante(self):
        return self.bursa

    def __str__(self):
        return f"{self.nume} are {self.varsta} ani si bursa: {self.bursa}"

# Deep copy vs shallow copy ( copiere adanca vs copiere superficiala )


# shallow copy retine referintele la elementele originale ( dar nu si pe cele adaugate dupa)
# deep copy copiaza recursiv toate elementele originale, dar fara referinte ( pastreaza o copie a obiectului original )

import copy

class Ceva:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'{self.a!r}, {self.b!r}'