### OOP - object oriented programming : Python (totul este un obiect)
### functionale: Lisp, Haskell > aproape toate operatiile sunt functii
### high-level, strongly typed : C, C++ ( a = 5 -> int a = 5; )

# OOP - mostenirea
class Persoana:  # clasa de baza
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def __str__(self):
        return f"{self.nume} are varsta {self.varsta}"


class Angajat(Persoana):  # clasa mostenita ( clasa copil ) -> mosteneste init si str
    def __init__(self, nume, varsta, salariu, ore_lucrate):
        Persoana.__init__(self, nume, varsta)  # super() -> adica superclass : clasa din care mostenim
        self.salariu = salariu
        self.ore_lucrate = ore_lucrate

    def arata_finante(self):
        return self.salariu * self.ore_lucrate


class Student(Persoana):  # clasa copil > mosteneste init si str
    def __init__(self, nume, varsta, bursa):
        Persoana.__init__(self, nume, varsta)
        self.bursa = bursa

    def arata_finante(self):
        return self.bursa

    @classmethod
    def create_from_string(cls, sablon: str): # cls este istanta clasei curente
        # Student.create_from_string("Ana 15 700")
        nume, varsta, bursa = sablon.split()
        varsta, bursa = int(varsta), int(bursa) # type casting (implementare int)
        if cls.is_name_corect(nume):
            return cls(nume, varsta, bursa)  # echivalent cu a zice asta: __init__(self, nume, varsta, bursa)

    @staticmethod
    def is_name_corect(nume):
        if nume[0].isupper() and len(nume) > 2:
            return True
        return False


class StudentMuncitor(Student, Angajat):  # ordinea conteaza! Primul mostenit este Student, apoi Angajat
    def __init__(self, nume, varsta, bursa, salariu, ore_lucrate):
        Student.__init__(self, nume, varsta, bursa)  # Student.__ -> instantiere anonima
        Angajat.__init__(self, nume, varsta, salariu, ore_lucrate)

    def arata_finante(self):
        return self.ore_lucrate * self.salariu + self.bursa

    def __str__(self):
        return f"{self.nume} a lucrat {self.ore_lucrate} ore si a castigat {self.salariu}$"


o1 = Persoana("George", 25)
o2 = Angajat("Andrei", 26, 1000, 40)
o3 = Student("Ion", 15, 800)
o4 = StudentMuncitor("Geo", 30, 800, 1200, 20)
print(o1)
print(o2)
print(o3)
print(o4)

o5 = Student.create_from_string("Razvan 30 1000")
print(o5)


# Razvan 20 9000
# Andrei 20 8900
# Alex   80 4000

# dunder methods : __dunder__
# p1 = Persoana("G", 5)
# class Simplu:
#    pass

# s = Simplu()
# __init__ self e null; __str__: null; __add__

# Persoana.__init__(self, nume, varsta) VS super().__init__(nume, varsta)
# super() -> Persoana -> self
# Persoana.__init__(self, nume, varsta)


# @classmethod : functie , dar se apeleaza pt intreaga instanta a clasei : poate modifica membrii sai ( ai clasei ), cls
# @staticmethod : functie, dar care e doar asociata clasei, nu este necesara instantiere unui obiect pt a o folosi. NU MODIFICA membrii clasei

class Matematica:

    @staticmethod
    def integrare():
        pass


Matematica.integrare()

###################################
# dataclasses
###################################
from dataclasses import dataclass


# valabil doar de la python 3.7 in sus
@dataclass
class Cineva:
    nume: list
    prenume: str

    # dataclass va creeaza automat dunder methods: __str__, __init__, __add__
    def afisare_nume_complet(self):
        return f"Eu sunt {self.nume} {self.prenume}!"


c1 = Cineva([1, 3], "Gheorghe")
print(c1.afisare_nume_complet())
c2 = Cineva([1], "Gheorghe")
print(c1 == c2)