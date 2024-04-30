# orice operatie pe fisier -> reprezinta un manafement de resurse ( resursa este chiar fisierul)
# ORICE RESURSA TREBUIE INITIALIZATA SI ELIBERATA cand este folosita

f = open("exemplu.txt", "w")
try:
    f.write("ceva")
except IOError:
    print("Error ocured")
finally:
    f.close()

# context manager : with
with open("exemplu.txt", "w") as fisier:
    fisier.write("altceva")


class FileManager:
    # def __int__, __enter__, __exit__
    def __init__(self, file_name, mod):
        self.mod = mod
        self.file_name = file_name
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, self.mod)
        print("Am intrat")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb): # exc_type -> are acces la type, exc_val -> valoare curenta, exc_tb traceback
        self.file.close()

with FileManager('exemplu1.txt', "w") as fisier2:
    fisier2.write("exemplu")


with FileManager('exemplu1.txt', "r") as fisier3:
     content = fisier3.read()
     print(content)